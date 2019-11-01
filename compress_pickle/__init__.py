from .compress_pickle import (
    dump,
    load,
    dumps,
    loads,
)
from .utils import (
    get_known_compressions,
    validate_compression,
    preprocess_path,
    open_compression_stream,
    get_default_compression_mapping,
    get_compression_write_mode,
    get_compression_read_mode,
    set_default_extensions,
    infer_compression_from_filename,
)

__version__ = "1.1.0"
