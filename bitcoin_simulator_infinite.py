#!/usr/bin/env python3
"""
INFINITE BITCOIN MAINNET SIMULATOR
===================================

This version runs FOREVER until you press Ctrl+C
"""

import sys
sys.path.insert(0, '/home/user/node')
from bitcoin_simulator import MainnetNode

def main():
    """Run infinite mainnet simulation"""
    node = MainnetNode()

    print("\n" + "=" * 70)
    print("🔄 INFINITE MAINNET SIMULATION")
    print("=" * 70)
    print("This will run FOREVER until you press Ctrl+C")
    print("=" * 70)
    print()

    block_count = 0
    try:
        while True:
            # Mine one block at a time
            block_count += 1
            print(f"\n{'='*70}")
            print(f"BLOCK #{block_count} (Height will be {node.chain_height + 1})")
            print(f"{'='*70}")

            node.generate_random_transactions()

            # Check for fork
            if not node.simulate_fork():
                node.mine_block()

            # Print status every 5 blocks
            if block_count % 5 == 0:
                node.print_network_status()

    except KeyboardInterrupt:
        print("\n\n🛑 INFINITE SIMULATION STOPPED BY USER")
        print("=" * 70)
        print(f"Total blocks mined: {block_count}")
        node.print_network_status()

if __name__ == "__main__":
    main()
