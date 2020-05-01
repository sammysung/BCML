""" Provides abstracted merging objects """
from abc import ABCMeta
from multiprocessing import Pool
from pathlib import Path
from typing import List, Union
from bcml import util

class Merger(metaclass=ABCMeta):
    """
    An abstract base class that represents a collection of merging functions for BCML. It can
    be subclassed to represent a single kind of merge, e.g. merging packs, game data, maps, etc.
    """
    NAME: str
    _friendly_name: str
    _description: str
    _log_name: str
    _options: dict
    _pool: Pool

    def __init__(self, friendly_name: str, description: str, log_name: str,
                 options: dict = None):
        self._friendly_name = friendly_name
        self._description = description
        self._log_name = log_name
        self._pool = None
        if options:
            self._options = options
        else:
            self._options = {}

    @property
    def friendly_name(self) -> str:
        """ The name of this merger in the UI """
        return self._friendly_name

    @property
    def description(self) -> str:
        """ The description of this merger in the UI """
        return self._description

    @property
    def log_name(self) -> str:
        """ The name of the log file created by this merger """
        return self._log_name

    def set_pool(self, pool: Pool):
        """ Sets the multiprocessing Pool to use when merging """
        self._pool = pool

    def set_options(self, options: dict):
        """ Sets custom options for this merger """
        self._options = options

    def generate_diff(self, mod_dir: Path, modded_files: List[Union[str, Path]]):
        """ Detects changes made to a modded file or files from the base game """
        raise NotImplementedError

    def log_diff(self, mod_dir: Path, diff_material):
        """ Saves generated diffs to a log file """
        raise NotImplementedError

    def is_mod_logged(self, mod: util.BcmlMod) -> bool:
        """ Checks if a mod is logged for this merge """
        return (mod.path / 'logs' / self._log_name).exists()

    def get_mod_diff(self, mod: util.BcmlMod):
        """ Gets the logged diff for this merge in a given mod """
        raise NotImplementedError

    def get_mod_edit_info(self, mod: util.BcmlMod) -> set:
        """ Gets a list of modified items in mod for this merger """
        raise NotImplementedError

    def get_all_diffs(self):
        """ Loads the installed diffs for this merge from all installed mods """
        raise NotImplementedError

    def consolidate_diffs(self, diffs: list):
        """ Combines and orders a collection of diffs into a single set of patches """
        raise NotImplementedError

    @staticmethod
    def can_partial_remerge() -> bool:
        """ Checks whether this merger can perform a partial remerge """
        return False

    @staticmethod
    def is_bootup_injector() -> bool:
        """ Checks whether this merger needs to inject a file into `Bootup.pack` """
        return False

    def get_bootup_injection(self) -> (str, bytes):
        """ Gets whatever file this merger needs to inject into `Bootup.pack` """
        raise NotImplementedError

    def get_mod_affected(self, mod: util.BcmlMod) -> []:
        """ Gets a list of files affected by a mod, if merger supports partial remerge """
        raise NotImplementedError

    def perform_merge(self):
        """ Applies one or more patches to the current mod installation """
        raise NotImplementedError

    def get_checkbox_options(self) -> List[tuple]:
        """ Gets the options for this merge as a tuple of internal name and UI description """
        return []

    def perform_unmerge(self):
        """ Performs any cleanup tasks needed when a merge mod is uninstalled """


def get_mergers() -> List[Merger]:
    """ Retrieves all available types of mod mergers """

    from bcml.mergers import (
        pack, texts, merge, data, mubin, events, rstable, actors, quests, effects
    )

    return [
        pack.PackMerger,
        merge.DeepMerger,
        texts.TextsMerger,
        actors.ActorInfoMerger,
        mubin.DungeonStaticMerger,
        mubin.MapMerger,
        data.GameDataMerger,
        data.SaveDataMerger,
        events.EventInfoMerger,
        effects.StatusEffectMerger,
        quests.QuestMerger,
        rstable.RstbMerger
    ]

def get_mergers_for_mod(mod: util.BcmlMod) -> List[Merger]:
    ms = []
    for m in [m() for m in get_mergers()]:
        if m.is_mod_logged(mod):
            ms.append(m)
    return ms


def sort_mergers(mergers: List[Merger]) -> List[Merger]:
    return sorted(mergers, key=lambda merger: merger.NAME == 'rstb', reverse=False)
