from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_files: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : Path
    ALL_REQUIRED_FILES : list