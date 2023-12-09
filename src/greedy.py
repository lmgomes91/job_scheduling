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
    def are_all_jobs_non_empty(service_orders: list[dict]) -> bool:
        for service_order in service_orders:
            if len(service_order['jobs']):
                return False
        return True

    def verify_process(self):
        keys_list = list(self.state_process.keys())
        for key in keys_list:
            if self.time == self.time_process[key]:
                self.state_process[key] = True

    def set_jobs(self, service_orders: list[dict]):

        for service_order in service_orders:
            if not len(service_order['jobs']):
                continue

            ready = True
            for machine in self.history_process:
                if len(self.history_process[machine]) and self.history_process[machine][-1] == service_order['id'] and \
                        self.time < self.time_process[machine]:
                    ready = False
                    break

            if ready and self.state_process[service_order['jobs'][0][0]]:
                self.state_process[service_order['jobs'][0][0]] = False
                self.time_process[service_order['jobs'][0][0]] = self.time + service_order['jobs'][0][1]
                self.history_process[service_order['jobs'][0][0]].append(service_order['id'])
                service_order['jobs'].pop(0)

    def run(self, data: list[dict]):

        interval = 10
        init = 0
        end = interval

        while True:
            service_orders = copy.deepcopy(data[init:end])

            while not self.are_all_jobs_non_empty(service_orders):

                self.set_jobs(service_orders)

                self.time += 1

                self.verify_process()

            init = end
            end += interval

            if init == 490:
                end = 497
            elif init == 497:
                break
        print(f'Total time: {self.time_process[max(self.time_process, key=self.time_process.get)]}')
