#!/usr/bin/env python3
#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - BAIN - MAIN ENTRY POINT                   ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        25/05/2026                        ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#                                                         ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#====================================================================================================# 

"""
Main entry point for the Twitter analysis pipeline.

Orchestrates:
1. Data loading (API or local)
2. Text cleaning
3. Hashtag analysis
4. Interaction graph construction
5. Network analysis
6. LLM prompt generation
7. Interactive LLM chat

Usage:
    python main.py                          # Load from CSV + full pipeline
    python main.py --api "#bitcoin" 200     # Load from API + full pipeline
    python main.py --no-llm                 # Skip LLM chat
    python main.py --help                   # Show options
"""

import argparse
import os
from pathlib import Path
from dotenv import load_dotenv

from data_extractor import DataExtractor


def main():
    """Main execution function."""
    
    parser = argparse.ArgumentParser(
        description="Twitter Analysis Pipeline – Bitcoin tweets",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--api", nargs="+", default=None,
        help="Load from RapidAPI instead of CSV. Usage: --api '#bitcoin' 200"
    )
    parser.add_argument(
        "--source", default="datasets/Bitcoin_tweets_dataset_2.csv",
        help="Path to CSV file (default: datasets/Bitcoin_tweets_dataset_2.csv)"
    )
    parser.add_argument(
        "--output", default="outputs",
        help="Output directory for results (default: outputs)"
    )
    parser.add_argument(
        "--no-llm", action="store_true",
        help="Skip LLM chat (run analysis only)"
    )
    parser.add_argument(
        "--model", default="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        help="LLM model to use (default: TinyLlama-1.1B)"
    )
    
    args = parser.parse_args()

    # Load environment variables (.env file)
    load_dotenv()

    print("\n" + "=" * 70)
    print("  TWITTER ANALYSIS PIPELINE - Unit 6 AEC2")
    print("=" * 70 + "\n")

    try:
        # Initialize extractor
        if args.api:
            # Load from API
            query = args.api[0]
            max_results = int(args.api[1]) if len(args.api) > 1 else 100
            
            print(f"[Main] Loading tweets from API (query: '{query}', max: {max_results})")
            extractor = DataExtractor()
            extractor.load_data_api(query, max_results, output_file="datasets/tweets_from_api.csv")
        else:
            # Load from CSV
            if not Path(args.source).exists():
                raise FileNotFoundError(f"File not found: {args.source}")
            
            print(f"[Main] Loading tweets from '{args.source}'")
            extractor = DataExtractor(source_file=args.source)
            extractor.load_data()

        # Execute pipeline
        extractor.execute_pipeline(
            output_dir=args.output,
            run_llm=not args.no_llm
        )

    except KeyboardInterrupt:
        print("\n\n[Main] Interrupted by user.")
    except Exception as e:
        print(f"\n[Main] ERROR: {e}")
        raise


if __name__ == "__main__":
    main()
