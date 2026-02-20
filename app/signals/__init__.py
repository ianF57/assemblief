"""Signals package exports."""

from app.signals.base_signal import BaseSignal, SignalCandidate
from app.signals.breakout_v1 import BreakoutV1
from app.signals.mean_reversion_v1 import MeanReversionV1
from app.signals.signal_manager import SignalManager
from app.signals.trend_signal_v1 import TrendSignalV1

__all__ = [
    "BaseSignal",
    "SignalCandidate",
    "TrendSignalV1",
    "MeanReversionV1",
    "BreakoutV1",
    "SignalManager",
]
