#!/usr/bin/env python3
"""
BITCOIN WALLET TRANSFER TOOL
=============================

Transfer simulated BTC between wallet addresses for testing.
"""

import sys
sys.path.insert(0, '/home/user/node')
from bitcoin_simulator import MainnetNode, Transaction

def transfer_bitcoin(from_address: str, to_address: str, amount: float, fee: float = 0.0001):
    """
    Transfer Bitcoin from one address to another

    Args:
        from_address: Source wallet address
        to_address: Destination wallet address
        amount: Amount of BTC to transfer
        fee: Transaction fee (default: 0.0001 BTC)
    """
    print("\n" + "=" * 70)
    print("💸 BITCOIN TRANSFER TOOL")
    print("=" * 70)

    # Create a node instance (this would typically connect to existing state)
    node = MainnetNode()

    print(f"\n📋 TRANSFER REQUEST:")
    print(f"   From:   {from_address}")
    print(f"   To:     {to_address}")
    print(f"   Amount: {amount:.8f} BTC")
    print(f"   Fee:    {fee:.8f} BTC")
    print(f"   Total:  {(amount + fee):.8f} BTC")

    # Check if source has funds (for simulation, we'll credit it if needed)
    current_balance = node.get_balance(from_address)
    print(f"\n💰 Current balance of {from_address}: {current_balance:.8f} BTC")

    if current_balance < (amount + fee):
        print(f"⚠️  Insufficient funds! Need {(amount + fee):.8f} BTC")
        print(f"🎁 Crediting {from_address} with initial funds for testing...")
        node.credit(from_address, amount + fee + 1.0)  # Add extra for future txs
        print(f"✅ New balance: {node.get_balance(from_address):.8f} BTC")

    # Create and add transaction
    tx = Transaction.create(from_address, to_address, amount, fee)

    print(f"\n🔨 Creating transaction...")
    print(f"   TX ID: {tx.txid}")

    if node.add_transaction(tx):
        print(f"✅ Transaction added to mempool!")

        # Show updated balances
        print(f"\n💰 UPDATED BALANCES:")
        print(f"   {from_address}: {node.get_balance(from_address):.8f} BTC")
        print(f"   {to_address}:   {node.get_balance(to_address):.8f} BTC")

        # Mine a block to confirm the transaction
        print(f"\n⛏️  Mining block to confirm transaction...")
        block = node.mine_block()

        print(f"\n✅ TRANSACTION CONFIRMED IN BLOCK {block.index}!")
        print(f"   Block Hash: {block.hash}")
        print(f"   Confirmations: 1")

        # Show final balances
        print(f"\n💰 FINAL BALANCES:")
        print(f"   {from_address}: {node.get_balance(from_address):.8f} BTC")
        print(f"   {to_address}:   {node.get_balance(to_address):.8f} BTC")

        return tx
    else:
        print(f"❌ Transaction failed! Insufficient balance.")
        return None


def interactive_transfer():
    """Interactive mode for transferring Bitcoin"""
    print("\n" + "=" * 70)
    print("💸 INTERACTIVE BITCOIN TRANSFER")
    print("=" * 70)

    from_addr = input("\nEnter source address (or press Enter for 'FoundryUSA'): ").strip()
    if not from_addr:
        from_addr = "FoundryUSA"

    to_addr = input("Enter destination address (or press Enter for 'MyWallet'): ").strip()
    if not to_addr:
        to_addr = "MyWallet"

    amount_str = input("Enter amount to transfer in BTC (or press Enter for 1.0): ").strip()
    amount = float(amount_str) if amount_str else 1.0

    fee_str = input("Enter transaction fee (or press Enter for 0.0001): ").strip()
    fee = float(fee_str) if fee_str else 0.0001

    transfer_bitcoin(from_addr, to_addr, amount, fee)


def quick_transfer_from_pools():
    """Quick transfer from mining pools to test wallets"""
    print("\n" + "=" * 70)
    print("🏊 QUICK TRANSFER FROM MINING POOLS")
    print("=" * 70)

    # Available mining pools
    pools = ["FoundryUSA", "AntPool", "F2Pool", "ViaBTC", "Binance", "Others"]

    print("\n📋 Available Mining Pools:")
    for i, pool in enumerate(pools, 1):
        print(f"   {i}. {pool}")

    pool_choice = input("\nSelect pool (1-6) or press Enter for FoundryUSA: ").strip()
    if pool_choice and pool_choice.isdigit():
        from_addr = pools[int(pool_choice) - 1]
    else:
        from_addr = "FoundryUSA"

    to_addr = input("Enter your wallet address (or press Enter for 'MyTestWallet'): ").strip()
    if not to_addr:
        to_addr = "MyTestWallet"

    amount_str = input("Enter BTC amount to transfer (default: 5.0): ").strip()
    amount = float(amount_str) if amount_str else 5.0

    print(f"\n🚀 Transferring {amount} BTC from {from_addr} to {to_addr}...")
    transfer_bitcoin(from_addr, to_addr, amount)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode
        if len(sys.argv) >= 4:
            from_addr = sys.argv[1]
            to_addr = sys.argv[2]
            amount = float(sys.argv[3])
            fee = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0001
            transfer_bitcoin(from_addr, to_addr, amount, fee)
        else:
            print("Usage: python3 bitcoin_transfer.py <from_address> <to_address> <amount> [fee]")
            print("\nExample:")
            print("  python3 bitcoin_transfer.py FoundryUSA MyWallet 10.5 0.0001")
    else:
        # Interactive mode
        print("\n" + "=" * 70)
        print("💸 BITCOIN TRANSFER TOOL - INTERACTIVE MODE")
        print("=" * 70)
        print("\nOptions:")
        print("  1. Quick transfer from mining pool")
        print("  2. Custom transfer")
        print("  3. Exit")

        choice = input("\nSelect option (1-3): ").strip()

        if choice == "1":
            quick_transfer_from_pools()
        elif choice == "2":
            interactive_transfer()
        else:
            print("Exiting...")
