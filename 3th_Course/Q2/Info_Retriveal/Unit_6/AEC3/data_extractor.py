#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - BAIN                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        08/04/2026  -  01:00:51           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    25/05/2026  -  REFACTORED        ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

"""
COMPATIBILITY WRAPPER
---------------------
This module reexports the DataExtractor class from the refactored core module.

The actual implementation is now organized in:
  - core/loader.py   : Data loading (API + local files)
  - core/cleaner.py  : Text cleaning and hashtag extraction
  - core/analyzer.py : NLP (sentiment, topics, summarization)
  - core/network.py  : NetworkX graph analysis
  - core/llm.py      : LLM interaction (local + API)
  - core/extractor.py: Main DataExtractor class

This file maintains backwards compatibility for existing code that imports:
    from data_extractor import DataExtractor
"""

from core import DataExtractor

__all__ = ["DataExtractor"]
