import pandas as pd


class Sequential:

    def __init__(self, convertedor: int, tratamento: int, lingotamento: int):

        self.convertedor = convertedor
        self.tratamento = tratamento
        self.lingotamento = lingotamento
        self.time = 0

    def validate_machine_total(self) -> None:
        if self.tratamento + self.convertedor + self.lingotamento > 11:
            raise 'Número de máquinas maior que 11'  # noqa

    @staticmethod
    def are_all_orders_non_empty(service_orders: list[dict]) -> bool:
        for service_order in service_orders:
            if len(service_order['jobs']):
                return False
        return True

    @staticmethod
    def clean_orders_done(service_orders: list[dict]):
        orders_to_remove = []
        for i in range(len(service_orders) - 1, 0, -1):
            if len(service_orders[i]['jobs']) == 0:
                orders_to_remove.append(i)

        for order in orders_to_remove:
            service_orders.pop(order)

    def verify_machines(self, machines: pd.DataFrame):
        for index, _ in machines.iterrows():
            if machines.at[index, 'time'] == self.time:
                machines.at[index, 'busy'] = False
                machines.at[index, 'actual_order'] = None

    def init_machines(self) -> pd.DataFrame:
        machine_list = []

        for _ in range(self.convertedor):
            machine_list.append({
                'name': 'CONVERTEDOR',
                'busy': False,
                'time': 0,
                'history': [],
                'actual_order': None
            })

        for _ in range(self.tratamento):
            machine_list.append({
                'name': 'TRATAMENTO',
                'busy': False,
                'time': 0,
                'history': [],
                'actual_order': None
            })

        for _ in range(self.tratamento):
            machine_list.append({
                'name': 'LINGOTAMENTO',
                'busy': False,
                'time': 0,
                'history': [],
                'actual_order': None
            })

        return pd.DataFrame(machine_list)

    def set_jobs(self, service_orders: list[dict], machines: pd.DataFrame):
        for i in range(0, len(service_orders)):
            if not len(service_orders[i]['jobs']) or (machines['actual_order'].isin([service_orders[i]['id']])).empty:
                continue

            free_machines = machines[
                (machines['busy'].isin([False])) &
                (machines['name'].isin([service_orders[i]['jobs'][0][0]]))
            ]

            if free_machines.empty:
                continue

            machines.at[free_machines.index[0], 'busy'] = True
            machines.at[free_machines.index[0], 'time'] = self.time + service_orders[i]['jobs'][0][1]
            machines.at[free_machines.index[0], 'history'].append(service_orders[i]['id'])
            machines.at[free_machines.index[0], 'actual_order'] = service_orders[i]['id']

            service_orders[i]['jobs'].pop(0)

    def run(self, data: list[dict]):
        self.validate_machine_total()

        machines = self.init_machines()

        orders_per_time = 10
        service_orders = data[:orders_per_time]
        data = data[orders_per_time:]

        while not self.are_all_orders_non_empty(service_orders):
            self.set_jobs(service_orders, machines)

            self.time += 1

            self.clean_orders_done(service_orders)

            while len(service_orders) < orders_per_time:
                if len(data):
                    service_orders.append(data.pop(0))
                else:
                    break

            self.verify_machines(machines)

        print(machines['time'].max())
