import json
from pathlib import Path
from dataclasses import dataclass
from enum import Enum

import pytest

from munazum.decision_log import log_decision, LOG_FILENAME


# --- Minimal stubs for testing ---

class Category(Enum):
    DOCUMENT = "document"


@dataclass
class FakePlanItem:
    source: Path
    destination: Path
    category: Category


# --- Tests ---

def test_log_decision_creates_log_file(tmp_path: Path):
    source = tmp_path / "file.txt"
    source.write_text("dummy")

    plan_item = FakePlanItem(
        source=source,
        destination=tmp_path / "dest" / "file.txt",
        category=Category.DOCUMENT,
    )

    log_decision(plan_item=plan_item, accepted=True)

    log_path = tmp_path / LOG_FILENAME
    assert log_path.exists()


def test_log_decision_writes_valid_json(tmp_path: Path):
    source = tmp_path / "file.txt"
    source.write_text("dummy")

    plan_item = FakePlanItem(
        source=source,
        destination=tmp_path / "dest" / "file.txt",
        category=Category.DOCUMENT,
    )

    log_decision(
        plan_item=plan_item,
        accepted=False,
        extra_features={"confidence": 0.87},
    )

    log_path = tmp_path / LOG_FILENAME
    line = log_path.read_text().strip()

    record = json.loads(line)

    assert record["accepted"] is False
    assert record["category"] == "document"
    assert record["features"]["confidence"] == 0.87
    assert "timestamp" in record
