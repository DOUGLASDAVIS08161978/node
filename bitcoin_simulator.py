#!/usr/bin/env python3
"""
SIMULATED FULL NODE + MINER WITH MAINNET SIMULATION
====================================================

Educational-only Bitcoin-style node and mining simulation with mainnet features:
- In-memory blockchain (no disk, no network)
- Multiple competing miners (simulating mainnet)
- Difficulty adjustment (like Bitcoin's 2016 block retargeting)
- Fork resolution (longest chain rule)
- Network propagation delays
- Simple mempool and wallet balances
- Proof-of-work style mining with adjustable difficulty

NO REAL BITCOIN. NO REAL NETWORK. PURELY EDUCATIONAL.
"""

import hashlib
import random
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from collections import defaultdict

# Mainnet-style configuration (scaled down for simulation)
INITIAL_DIFFICULTY = 3          # Starting difficulty (leading zeros)
MAX_DIFFICULTY = 6              # Maximum difficulty
DIFFICULTY_ADJUSTMENT_INTERVAL = 10  # Blocks between difficulty adjustments (Bitcoin: 2016)
TARGET_BLOCK_TIME = 10          # Target seconds per block (Bitcoin: 600 seconds = 10 minutes)
BLOCK_REWARD = 6.25             # Simulated BTC (current Bitcoin reward)
HALVING_INTERVAL = 210000       # Blocks between halvings (same as Bitcoin)
NETWORK_PROPAGATION_DELAY = 1.5 # Seconds to simulate network propagation


@dataclass
class Transaction:
    txid: str
    from_addr: str
    to_addr: str
    amount: float
    fee: float
    timestamp: float

    @staticmethod
    def create(from_addr: str, to_addr: str, amount: float, fee: float = 0.0001) -> "Transaction":
        now = time.time()
        raw = f"{from_addr}{to_addr}{amount}{fee}{now}{random.random()}"
        txid = hashlib.sha256(raw.encode()).hexdigest()
        return Transaction(
            txid=txid,
            from_addr=from_addr,
            to_addr=to_addr,
            amount=amount,
            fee=fee,
            timestamp=now,
        )


@dataclass
class Block:
    index: int
    previous_hash: str
    timestamp: float
    nonce: int
    difficulty: int
    miner_address: str
    transactions: List[Transaction] = field(default_factory=list)
    hash: str = ""

    def header(self) -> str:
        tx_root = hashlib.sha256(
            "".join(tx.txid for tx in self.transactions).encode()
        ).hexdigest()
        return f"{self.index}{self.previous_hash}{self.timestamp}{self.nonce}{self.difficulty}{self.miner_address}{tx_root}"

    def compute_hash(self) -> str:
        return hashlib.sha256(self.header().encode()).hexdigest()

    def meets_difficulty(self) -> bool:
        return self.hash.startswith("0" * self.difficulty)


class MiningPool:
    """Represents a mining pool on the simulated mainnet"""
    def __init__(self, name: str, hashrate_percentage: float):
        self.name = name
        self.hashrate_percentage = hashrate_percentage  # % of total network hashrate
        self.blocks_mined = 0
        self.total_rewards = 0.0

    def __repr__(self):
        return f"MiningPool({self.name}, {self.hashrate_percentage}% hashrate, {self.blocks_mined} blocks)"


class MainnetNode:
    """Simulated Bitcoin mainnet node with multiple miners"""

    def __init__(self):
        self.chain: List[Block] = []
        self.alternative_chains: List[List[Block]] = []  # For forks
        self.mempool: List[Transaction] = []
        self.wallets: Dict[str, float] = {}
        self.current_difficulty = INITIAL_DIFFICULTY

        # Mining pools (simulating mainnet distribution)
        self.mining_pools = [
            MiningPool("FoundryUSA", 28.0),
            MiningPool("AntPool", 18.0),
            MiningPool("F2Pool", 15.0),
            MiningPool("ViaBTC", 12.0),
            MiningPool("Binance", 10.0),
            MiningPool("Others", 17.0),
        ]

        # Statistics
        self.total_fees_collected = 0.0
        self.orphaned_blocks = 0
        self.forks_resolved = 0

        self._create_genesis_block()

    # ---------- Blockchain basics ----------

    def _create_genesis_block(self):
        """Create the genesis block (block 0)"""
        genesis = Block(
            index=0,
            previous_hash="0" * 64,
            timestamp=time.time(),
            nonce=0,
            difficulty=INITIAL_DIFFICULTY,
            miner_address="SATOSHI_NAKAMOTO",
            transactions=[],
        )
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)
        print("=" * 70)
        print("🌍 BITCOIN MAINNET SIMULATION INITIALIZED")
        print("=" * 70)
        print(f"🌱 Genesis block created")
        print(f"   Hash: {genesis.hash}")
        print(f"   Difficulty: {INITIAL_DIFFICULTY}")
        print(f"   Mining pools: {len(self.mining_pools)}")
        print()

    @property
    def latest_block(self) -> Block:
        return self.chain[-1]

    @property
    def chain_height(self) -> int:
        return len(self.chain) - 1

    def is_chain_valid(self) -> bool:
        """Validate the entire blockchain"""
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            # Check hash is correct
            if curr.hash != curr.compute_hash():
                return False

            # Check meets difficulty
            if not curr.meets_difficulty():
                return False

            # Check links to previous block
            if curr.previous_hash != prev.hash:
                return False
        return True

    # ---------- Difficulty adjustment ----------

    def adjust_difficulty(self):
        """Adjust difficulty based on recent block times (like Bitcoin)"""
        if self.chain_height % DIFFICULTY_ADJUSTMENT_INTERVAL != 0 or self.chain_height == 0:
            return

        # Calculate actual time for last DIFFICULTY_ADJUSTMENT_INTERVAL blocks
        interval_start = max(0, len(self.chain) - DIFFICULTY_ADJUSTMENT_INTERVAL - 1)
        actual_time = self.chain[-1].timestamp - self.chain[interval_start].timestamp
        expected_time = DIFFICULTY_ADJUSTMENT_INTERVAL * TARGET_BLOCK_TIME

        old_difficulty = self.current_difficulty

        # Adjust difficulty up or down
        if actual_time < expected_time * 0.75 and self.current_difficulty < MAX_DIFFICULTY:
            # Blocks coming too fast, increase difficulty
            self.current_difficulty += 1
            print(f"\n⚡ DIFFICULTY INCREASED: {old_difficulty} → {self.current_difficulty}")
            print(f"   Blocks were mined {expected_time/actual_time:.2f}x too fast")
        elif actual_time > expected_time * 1.5 and self.current_difficulty > 1:
            # Blocks coming too slow, decrease difficulty
            self.current_difficulty -= 1
            print(f"\n🐌 DIFFICULTY DECREASED: {old_difficulty} → {self.current_difficulty}")
            print(f"   Blocks were mined {actual_time/expected_time:.2f}x too slow")

    # ---------- Wallet / mempool ----------

    def get_balance(self, address: str) -> float:
        return self.wallets.get(address, 0.0)

    def credit(self, address: str, amount: float):
        self.wallets[address] = self.get_balance(address) + amount

    def debit(self, address: str, amount: float) -> bool:
        if self.get_balance(address) >= amount:
            self.wallets[address] -= amount
            return True
        return False

    def add_transaction(self, tx: Transaction) -> bool:
        """Add transaction to mempool with validation"""
        if tx.amount <= 0 or tx.fee < 0:
            return False

        if tx.from_addr != "COINBASE":
            total_needed = tx.amount + tx.fee
            if not self.debit(tx.from_addr, total_needed):
                return False

        self.mempool.append(tx)
        return True

    def get_current_block_reward(self) -> float:
        """Calculate current block reward (includes halving)"""
        halvings = self.chain_height // HALVING_INTERVAL
        return BLOCK_REWARD / (2 ** halvings)

    # ---------- Mining (with multiple pools) ----------

    def select_mining_pool(self) -> MiningPool:
        """Select which pool mines the next block based on hashrate distribution"""
        rand = random.random() * 100
        cumulative = 0
        for pool in self.mining_pools:
            cumulative += pool.hashrate_percentage
            if rand <= cumulative:
                return pool
        return self.mining_pools[-1]  # Fallback

    def mine_block(self, mining_pool: Optional[MiningPool] = None) -> Block:
        """Mine a new block (simulating mainnet mining)"""
        if mining_pool is None:
            mining_pool = self.select_mining_pool()

        # Select transactions from mempool (prioritize by fee)
        self.mempool.sort(key=lambda tx: tx.fee, reverse=True)
        selected_txs: List[Transaction] = []
        max_txs = min(10, len(self.mempool))
        total_fees = 0.0

        for _ in range(max_txs):
            if self.mempool:
                tx = self.mempool.pop(0)
                selected_txs.append(tx)
                total_fees += tx.fee

        # Add coinbase transaction (block reward + fees)
        current_reward = self.get_current_block_reward()
        coinbase = Transaction.create(
            from_addr="COINBASE",
            to_addr=mining_pool.name,
            amount=current_reward + total_fees,
            fee=0.0,
        )
        selected_txs.insert(0, coinbase)

        # Create candidate block
        new_index = self.latest_block.index + 1
        candidate = Block(
            index=new_index,
            previous_hash=self.latest_block.hash,
            timestamp=time.time(),
            nonce=0,
            difficulty=self.current_difficulty,
            miner_address=mining_pool.name,
            transactions=selected_txs,
        )

        print(f"\n⛏️  [{mining_pool.name}] Mining block {new_index}...")
        print(f"   Transactions: {len(selected_txs)} (fees: {total_fees:.8f} BTC)")
        print(f"   Difficulty: {self.current_difficulty} leading zeros")
        start = time.time()

        # Proof of work
        attempts = 0
        while True:
            candidate_hash = candidate.compute_hash()
            if candidate_hash.startswith("0" * self.current_difficulty):
                candidate.hash = candidate_hash
                break
            candidate.nonce += 1
            attempts += 1

        elapsed = time.time() - start

        # Simulate network propagation delay
        time.sleep(random.uniform(0, NETWORK_PROPAGATION_DELAY))

        # Add to chain
        self.chain.append(candidate)

        # Update statistics
        mining_pool.blocks_mined += 1
        mining_pool.total_rewards += current_reward + total_fees
        self.total_fees_collected += total_fees

        # Credit the mining pool
        self.credit(mining_pool.name, current_reward + total_fees)

        # Credit recipients of all transactions in the block
        for tx in selected_txs:
            if tx.from_addr != "COINBASE":  # Skip coinbase (already credited above)
                self.credit(tx.to_addr, tx.amount)

        print(f"✅ Block {new_index} mined in {elapsed:.2f}s ({attempts:,} attempts)")
        print(f"   Hash:   {candidate.hash}")
        print(f"   Reward: {current_reward:.8f} BTC + {total_fees:.8f} fees")
        print(f"   Pool:   {mining_pool.name}")

        # Check for difficulty adjustment
        self.adjust_difficulty()

        return candidate

    # ---------- Fork simulation ----------

    def simulate_fork(self) -> bool:
        """Occasionally simulate a fork (2 blocks found simultaneously)"""
        if random.random() < 0.15:  # 15% chance of fork
            print("\n" + "!" * 70)
            print("🔱 FORK DETECTED! Two miners found blocks simultaneously")
            print("!" * 70)

            # Two different pools mine competing blocks
            pool1 = self.select_mining_pool()
            pool2 = self.select_mining_pool()
            while pool2 == pool1:
                pool2 = self.select_mining_pool()

            print(f"   Chain A: {pool1.name}")
            print(f"   Chain B: {pool2.name}")

            # Save current chain
            original_chain = self.chain.copy()

            # Mine block on chain A
            self.chain = original_chain.copy()
            block_a = self.mine_block(pool1)
            chain_a = self.chain.copy()

            # Mine block on chain B (revert first)
            self.chain = original_chain.copy()
            block_b = self.mine_block(pool2)
            chain_b = self.chain.copy()

            # Next block resolves the fork (longest chain wins)
            print(f"\n   ⛏️  Mining to resolve fork...")
            if random.random() < 0.5:
                # Chain A wins
                self.chain = chain_a
                winning_pool = self.select_mining_pool()
                self.mine_block(winning_pool)
                print(f"\n   ✅ Chain A wins! Block by {pool2.name} orphaned")
                self.orphaned_blocks += 1
            else:
                # Chain B wins
                self.chain = chain_b
                winning_pool = self.select_mining_pool()
                self.mine_block(winning_pool)
                print(f"\n   ✅ Chain B wins! Block by {pool1.name} orphaned")
                self.orphaned_blocks += 1

            self.forks_resolved += 1
            return True

        return False

    # ---------- Simulation ----------

    def generate_random_transactions(self):
        """Generate random transactions simulating mainnet activity"""
        # High activity - more transactions
        num_txs = random.randint(5, 15)

        for _ in range(num_txs):
            from_addr = f"user_{random.randint(1, 100)}"
            to_addr = f"user_{random.randint(1, 100)}"
            amount = round(random.uniform(0.001, 1.0), 8)
            fee = round(random.uniform(0.00001, 0.001), 8)

            # Seed balances
            if self.get_balance(from_addr) < amount + fee:
                self.credit(from_addr, (amount + fee) * 2)

            tx = Transaction.create(from_addr, to_addr, amount, fee)
            if self.add_transaction(tx):
                if random.random() < 0.1:  # Only print 10% of txs to reduce spam
                    print(f"   💰 Tx: {from_addr} → {to_addr} : {amount:.8f} BTC (fee: {fee:.8f})")

    def print_network_status(self):
        """Print comprehensive mainnet simulation status"""
        b = self.latest_block
        print("\n" + "=" * 70)
        print("📊 MAINNET STATUS")
        print("=" * 70)
        print(f"Block Height:     {self.chain_height:,}")
        print(f"Latest Hash:      {b.hash}")
        print(f"Difficulty:       {self.current_difficulty} leading zeros")
        print(f"Block Reward:     {self.get_current_block_reward():.8f} BTC")
        print(f"Mempool Size:     {len(self.mempool)} transactions")
        print(f"Chain Valid:      {self.is_chain_valid()}")
        print(f"Forks Resolved:   {self.forks_resolved}")
        print(f"Orphaned Blocks:  {self.orphaned_blocks}")
        print(f"Total Fees:       {self.total_fees_collected:.8f} BTC")

        print("\n🏊 MINING POOL STATISTICS:")
        for pool in sorted(self.mining_pools, key=lambda p: p.blocks_mined, reverse=True):
            balance = self.get_balance(pool.name)
            print(f"   {pool.name:20s} | Blocks: {pool.blocks_mined:3d} | "
                  f"Balance: {balance:10.8f} BTC | "
                  f"Hashrate: {pool.hashrate_percentage:5.1f}%")
        print("=" * 70)

    def run_simulation(self, num_blocks: int = 50):
        """Run the mainnet simulation for a specific number of blocks"""
        print(f"\n🚀 STARTING MAINNET SIMULATION ({num_blocks} blocks)\n")

        try:
            for i in range(num_blocks):
                # Generate network activity
                print(f"\n--- Round {i+1}/{num_blocks} ---")
                self.generate_random_transactions()

                # Check for fork
                if not self.simulate_fork():
                    # Normal mining (no fork)
                    self.mine_block()

                # Print status every 5 blocks
                if (i + 1) % 5 == 0:
                    self.print_network_status()

                # Small delay between blocks
                time.sleep(0.5)

            # Final statistics
            print("\n" + "=" * 70)
            print("🏁 SIMULATION COMPLETE")
            print("=" * 70)
            self.print_network_status()

        except KeyboardInterrupt:
            print("\n\n🛑 Simulation stopped by user")
            self.print_network_status()


def main():
    """Run the mainnet simulation"""
    node = MainnetNode()

    # Run simulation for 30 blocks (can be changed)
    node.run_simulation(num_blocks=30)


if __name__ == "__main__":
    main()
