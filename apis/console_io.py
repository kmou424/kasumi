import sys


def __flush_stdout():
    sys.stdout.flush()


def args_num_error(cmd: str):
    sys.stdout.write("{cmd}: Too many/few argument(s), please recheck your command!\n".format(cmd=cmd))
    __flush_stdout()


def args_type_error(cmd: str):
    sys.stdout.write("{cmd}: Wrong argument(s), please recheck your command!\n".format(cmd=cmd))
    __flush_stdout()


def args_id_out_of_bounds_error(cmd: str, ids: str):
    sys.stdout.write("{cmd}: ID {id} out of bounds, please recheck your command!\n".format(cmd=cmd, id=ids))
    __flush_stdout()
