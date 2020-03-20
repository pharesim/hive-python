import hive as hve
import sys

_shared_hived_instance = None


def get_config_node_list():
    from hivebase.storage import configStorage
    nodes = configStorage.get('nodes', None)
    if nodes:
        return nodes.split(',')


def shared_hived_instance():
    """ This method will initialize _shared_hived_instance and return it.
    The purpose of this method is to have offer single default Hive
    instance that can be reused by multiple classes.  """

    global _shared_hived_instance
    if not _shared_hived_instance:
        if sys.version >= '3.0':
            _shared_hived_instance = hve.hived.Hived(
                nodes=get_config_node_list())
        else:
            _shared_hived_instance = hve.Hived(
                nodes=get_config_node_list())
    return _shared_hived_instance


def set_shared_hived_instance(hived_instance):
    """ This method allows us to override default hive instance for all
    users of _shared_hived_instance.  """

    global _shared_hived_instance
    _shared_hived_instance = hived_instance
