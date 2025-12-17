#!/usr/bin/env python3
"""
Quick test of the Bitcoin Mainnet Simulator - runs 10 blocks then exits
"""

import sys
sys.path.insert(0, '/home/user/node')
from bitcoin_simulator import MainnetNode

def test_mainnet_simulation():
    """Test basic mainnet node and mining functionality"""
    print("=" * 70)
    print("TESTING BITCOIN MAINNET SIMULATOR")
    print("=" * 70)

    node = MainnetNode()

    # Verify genesis block
    assert len(node.chain) == 1, "Should have genesis block"
    assert node.chain[0].index == 0, "Genesis should be block 0"
    print("✓ Genesis block created successfully")

    # Run simulation for 10 blocks
    print("\n" + "=" * 70)
    print("Running 10-block simulation...")
    print("=" * 70)
    node.run_simulation(num_blocks=10)

    # Validate results
    assert len(node.chain) == 11, f"Should have 11 blocks (genesis + 10), has {len(node.chain)}"
    assert node.is_chain_valid(), "Chain should be valid"
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED")
    print("=" * 70)

    return True

if __name__ == "__main__":
    try:
        test_mainnet_simulation()
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
