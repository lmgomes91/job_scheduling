import copy


class Greedy:
    def __init__(self):
        self.state_process = {
            'CV01': True,
            'CV02': True,
            'FPA01': True,
            'FPA02': True,
            'RH01': True,
            'CC01': True,
            'CC02': True,
            'CL03': True,
            'CL11': True,
            'CL15': True,
            'CL21': True
        }

        self.time_process = {
            'CV01': 0,
            'CV02': 0,
            'FPA01': 0,
            'FPA02': 0,
            'RH01': 0,
            'CC01': 0,
            'CC02': 0,
            'CL03': 0,
            'CL11': 0,
            'CL15': 0,
            'CL21': 0
        }

        self.history_process = {
            'CV01': [],
            'CV02': [],
            'FPA01': [],
            'FPA02': [],
            'RH01': [],
            'CC01': [],
            'CC02': [],
            'CL03': [],
            'CL11': [],
            'CL15': [],
            'CL21': []
        }

        self.time = 0

    @staticmethod
    def are_all_orders_non_empty(service_orders: list[dict]) -> bool:
        for service_order in service_orders:
            if len(service_order['jobs']):
                return False
        return True

    def verify_process(self):
        keys_list = list(self.state_process.keys())
        for key in keys_list:
            if self.time == self.time_process[key]:
                self.state_process[key] = True

    def verify_job_ready(self, service_order: dict):
        for process in self.history_process:
            if len(self.history_process[process]) and \
                    self.history_process[process][-1] == service_order['id'] and \
                    self.time < self.time_process[process]:
                return False
        return True

    def set_jobs(self, service_orders: list[dict]):

        order_candidate = {
            'CV01': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CV02': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'FPA01': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'FPA02': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'RH01': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CC01': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CC02': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CL03': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CL11': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CL15': {
                'id': 0,
                'time': 0,
                'service_index': 0
            },
            'CL21': {
                'id': 0,
                'time': 0,
                'service_index': 0
            }
        }

        for i in range(0, len(service_orders)):
            if not len(service_orders[i]['jobs']) or \
                    not self.verify_job_ready(service_orders[i]) or \
                    not self.state_process[service_orders[i]['jobs'][0][0]]:
                continue

            if order_candidate[service_orders[i]['jobs'][0][0]]['id'] == 0:
                order_candidate[service_orders[i]['jobs'][0][0]] = {
                    'id': service_orders[i]['id'],
                    'time': service_orders[i]['jobs'][0][1],
                    'service_index': i
                }
            elif order_candidate[service_orders[i]['jobs'][0][0]]['time'] > service_orders[i]['jobs'][0][1]:
                order_candidate[service_orders[i]['jobs'][0][0]] = {
                    'id': service_orders[i]['id'],
                    'time': service_orders[i]['jobs'][0][1],
                    'service_index': i
                }

        for key in order_candidate:
            if order_candidate[key]['id'] != 0:
                self.state_process[key] = False
                self.time_process[key] = self.time + order_candidate[key]['time']
                self.history_process[key].append(order_candidate[key]['id'])
                service_orders[order_candidate[key]['service_index']]['jobs'].pop(0)

    @staticmethod
    def clean_orders_done(service_orders: list[dict]):
        orders_to_remove = []
        for i in range(len(service_orders) - 1, 0, -1):
            if len(service_orders[i]['jobs']) == 0:
                orders_to_remove.append(i)

        for order in orders_to_remove:
            service_orders.pop(order)

    def run(self, data: list[dict]):
        orders_per_time = 10
        service_orders = data[:orders_per_time]
        data = data[orders_per_time:]

        while not self.are_all_orders_non_empty(service_orders):

            self.set_jobs(service_orders)

            self.time += 1

            self.clean_orders_done(service_orders)

            while len(service_orders) < orders_per_time:
                if len(data):
                    service_orders.append(data.pop(0))
                else:
                    break

            self.verify_process()

        print(f'Total time: {self.time_process[max(self.time_process, key=self.time_process.get)]}')
