"""
Master entry point
"""


def run_rest_service():
    """
    Run rest as in a thread function
    """
    from .rest_service import RESTService
    rest = RESTService()
    rest.run()


if __name__ == '__main__':
    """
    Entry point
    """
    print("Running Harmonic Master")

    # Load configuration from file
    from .configuration import Setting
    Setting.read_cfg_from_file()

    # Print instance information
    print("Node name: {0}\nNode address: {1}".format(Setting.get_node_name(), Setting.get_node_addr()))
    print("Port range: {0} to {1} ({2} ports available) ".format(Setting.get_data_port_start(),
                                                                 Setting.get_data_port_stop(),
                                                                 Setting.get_data_port_stop() -
                                                                 Setting.get_data_port_start()))

    # Create thread for handling REST Service
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor()

    # Binding commander to the rest service and enable REST service
    pool.submit(run_rest_service)