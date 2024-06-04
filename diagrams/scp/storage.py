# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _Scp


class _Storage(_Scp):
    _type = "storage"
    _icon_dir = "resources/scp/storage"


class Archivestorage(_Storage):
    _icon = "ArchiveStorage.png"


class Backup(_Storage):
    _icon = "Backup.png"


class Blockstorage_Bm(_Storage):
    _icon = "BlockStorage_BM.png"


class Blockstorage_Vm(_Storage):
    _icon = "BlockStorage_VM.png"


class Filestorage(_Storage):
    _icon = "FileStorage.png"


class Objectstorage(_Storage):
    _icon = "ObjectStorage.png"


# Aliases