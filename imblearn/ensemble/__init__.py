"""
The :mod:`imblearn.ensemble` module include methods generating
under-sampled subsets combined inside an ensemble.
"""

from ._easy_ensemble import EasyEnsemble
from ._balance_cascade import BalanceCascade

from ._classifier import BalancedBaggingClassifier

__all__ = ['EasyEnsemble', 'BalancedBaggingClassifier', 'BalanceCascade']
