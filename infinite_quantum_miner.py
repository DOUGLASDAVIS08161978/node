#!/usr/bin/env python3
"""
BITCOIN MAINNET MINING SIMULATOR - INFINITE LOOP WITH MEMPOOL INTEGRATION
==========================================================================

Real-world Bitcoin mining simulation with Mempool-style output:
- Live blockchain explorer interface
- Real-time mempool monitoring
- Network statistics and health metrics
- Fee rate estimation
- Block propagation tracking
- Peer network simulation
- Geographic mining distribution

ALL REWARDS → bc1qfzhx87ckhn4tnkswhsth56h0gm5we4hdq5wass

NO REAL BITCOIN. PURELY EDUCATIONAL SIMULATION.
"""

import hashlib
import random
import time
import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from collections import defaultdict
from datetime import datetime
import sys


# Configuration
INITIAL_DIFFICULTY = 4
MAX_DIFFICULTY = 8
DIFFICULTY_ADJUSTMENT_INTERVAL = 10
TARGET_BLOCK_TIME = 2  # seconds (faster for demonstration)
BLOCK_REWARD = 6.25
HALVING_INTERVAL = 210000
REWARD_WALLET = "bc1qfzhx87ckhn4tnkswhsth56h0gm5we4hdq5wass"


@dataclass
class QuantumDevice:
    """Quantum/supercomputer mining device"""
    device_id: str
    device_type: str
    manufacturer: str
    qubit_count: int
    hashrate_ehs: float
    location: str
    ip_address: str
    country: str
    latitude: float
    longitude: float

    def __repr__(self):
        return f"{self.device_type} ({self.hashrate_ehs} EH/s) @ {self.location}"


@dataclass
class Transaction:
    txid: str
    from_addr: str
    to_addr: str
    amount: float
    fee: float
    timestamp: float
    size_bytes: int
    fee_rate: float  # sat/vB

    @staticmethod
    def create(from_addr: str, to_addr: str, amount: float, fee: float = None):
        now = time.time()
        raw = f"{from_addr}{to_addr}{amount}{now}{random.random()}"
        txid = hashlib.sha256(raw.encode()).hexdigest()

        # Random transaction size
        size_bytes = random.randint(200, 500)

        # Auto-calculate fee if not provided
        if fee is None:
            fee_rate = random.uniform(1, 50)  # sat/vB
            fee = (fee_rate * size_bytes) / 100000000  # Convert to BTC
        else:
            fee_rate = (fee * 100000000) / size_bytes

        return Transaction(
            txid=txid,
            from_addr=from_addr,
            to_addr=to_addr,
            amount=amount,
            fee=fee,
            timestamp=now,
            size_bytes=size_bytes,
            fee_rate=fee_rate
        )


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    previous_hash: str
    nonce: int
    hash: str
    difficulty: int
    miner: str
    reward: float
    size_bytes: int
    weight: int
    quantum_device: QuantumDevice


class MempoolSimulator:
    """Simulates Bitcoin mempool with realistic metrics"""

    def __init__(self):
        self.pending_txs: List[Transaction] = []
        self.tx_count_history = []
        self.fee_rate_history = []

    def add_transaction(self, tx: Transaction):
        """Add transaction to mempool"""
        self.pending_txs.append(tx)

    def remove_transactions(self, txs: List[Transaction]):
        """Remove mined transactions from mempool"""
        for tx in txs:
            if tx in self.pending_txs:
                self.pending_txs.remove(tx)

    def get_size(self) -> int:
        """Get mempool size in bytes"""
        return sum(tx.size_bytes for tx in self.pending_txs)

    def get_fee_rates(self) -> Dict[str, float]:
        """Get recommended fee rates for different priorities"""
        if not self.pending_txs:
            return {"high": 1.0, "medium": 1.0, "low": 1.0}

        fee_rates = sorted([tx.fee_rate for tx in self.pending_txs], reverse=True)

        return {
            "high": fee_rates[0] if fee_rates else 1.0,
            "medium": fee_rates[len(fee_rates)//2] if len(fee_rates) > 1 else 1.0,
            "low": fee_rates[-1] if fee_rates else 1.0
        }

    def print_mempool_status(self):
        """Print mempool statistics (Mempool-style)"""
        tx_count = len(self.pending_txs)
        size_mb = self.get_size() / 1_000_000
        fee_rates = self.get_fee_rates()

        print(f"\n{'─'*80}")
        print(f"📊 MEMPOOL STATUS")
        print(f"{'─'*80}")
        print(f"Transactions:        {tx_count:,} txs")
        print(f"Size:                {size_mb:.2f} MB")
        print(f"")
        print(f"💰 FEE ESTIMATES (sat/vB):")
        print(f"   High Priority:    {fee_rates['high']:.1f} sat/vB (~10 min)")
        print(f"   Medium Priority:  {fee_rates['medium']:.1f} sat/vB (~30 min)")
        print(f"   Low Priority:     {fee_rates['low']:.1f} sat/vB (~1 hour)")
        print(f"{'─'*80}")


class InfiniteQuantumMiner:
    """Infinite loop quantum Bitcoin miner with Mempool integration"""

    def __init__(self, reward_wallet: str):
        self.chain: List[Block] = []
        self.mempool = MempoolSimulator()
        self.balances = defaultdict(float)
        self.difficulty = INITIAL_DIFFICULTY
        self.reward_wallet = reward_wallet
        self.total_rewards = 0.0
        self.blocks_mined = 0
        self.total_hashrate_ehs = 0.0

        # Network stats
        self.peer_count = random.randint(80, 150)
        self.network_hashrate_ehs = 0.0

        # Initialize quantum devices
        self.quantum_devices = self._initialize_quantum_devices()
        self.total_hashrate_ehs = sum(d.hashrate_ehs for d in self.quantum_devices)

        # Create genesis
        self._create_genesis()

        print(f"\n{'='*80}")
        print(f"⚛️  BITCOIN MAINNET QUANTUM MINING SIMULATOR - INFINITE LOOP")
        print(f"{'='*80}")
        print(f"🎯 Reward Wallet: {reward_wallet}")
        print(f"⚛️  Quantum Devices: {len(self.quantum_devices)}")
        print(f"💪 Total Hashrate: {self.total_hashrate_ehs:.2f} EH/s")
        print(f"🌐 Network Peers: {self.peer_count}")
        print(f"⏱️  Target Block Time: {TARGET_BLOCK_TIME}s")
        print(f"{'='*80}")
        print()

    def _initialize_quantum_devices(self) -> List[QuantumDevice]:
        """Initialize quantum mining devices with geographic data"""
        devices = [
            QuantumDevice(
                device_id="IBM-Q-CONDOR-001",
                device_type="IBM Quantum Condor",
                manufacturer="IBM",
                qubit_count=1121,
                hashrate_ehs=45.5,
                location="Yorktown Heights, NY, USA",
                ip_address="170.25.142.88",
                country="USA",
                latitude=41.2701,
                longitude=-73.8090
            ),
            QuantumDevice(
                device_id="GOOGLE-WILLOW-001",
                device_type="Google Willow",
                manufacturer="Google",
                qubit_count=105,
                hashrate_ehs=125.7,
                location="Santa Barbara, CA, USA",
                ip_address="172.217.14.229",
                country="USA",
                latitude=34.4208,
                longitude=-119.6982
            ),
            QuantumDevice(
                device_id="IONQ-ARIA-001",
                device_type="IonQ Aria",
                manufacturer="IonQ",
                qubit_count=25,
                hashrate_ehs=89.3,
                location="College Park, MD, USA",
                ip_address="162.250.191.14",
                country="USA",
                latitude=38.9807,
                longitude=-76.9369
            ),
            QuantumDevice(
                device_id="DWAVE-ADVANTAGE-001",
                device_type="D-Wave Advantage",
                manufacturer="D-Wave",
                qubit_count=5640,
                hashrate_ehs=215.4,
                location="Burnaby, BC, Canada",
                ip_address="206.12.94.33",
                country="Canada",
                latitude=49.2488,
                longitude=-122.9805
            ),
            QuantumDevice(
                device_id="FRONTIER-001",
                device_type="Frontier Exascale",
                manufacturer="HPE/AMD",
                qubit_count=0,
                hashrate_ehs=312.5,
                location="Oak Ridge, TN, USA",
                ip_address="160.91.234.56",
                country="USA",
                latitude=36.0103,
                longitude=-84.2696
            ),
            QuantumDevice(
                device_id="FUGAKU-001",
                device_type="Fugaku Supercomputer",
                manufacturer="Fujitsu",
                qubit_count=0,
                hashrate_ehs=278.9,
                location="Kobe, Japan",
                ip_address="133.1.138.202",
                country="Japan",
                latitude=34.6901,
                longitude=135.1955
            ),
        ]
        return devices

    def _create_genesis(self):
        """Create genesis block"""
        genesis_tx = Transaction.create("GENESIS", "GENESIS", 0, 0)
        genesis = Block(
            index=0,
            timestamp=time.time(),
            transactions=[genesis_tx],
            previous_hash="0" * 64,
            nonce=0,
            hash="",
            difficulty=self.difficulty,
            miner=self.reward_wallet,
            reward=0,
            size_bytes=285,
            weight=1140,
            quantum_device=self.quantum_devices[0]
        )
        genesis.hash = self._calculate_hash(genesis)
        self.chain.append(genesis)

    def _calculate_hash(self, block: Block) -> str:
        """Calculate block hash"""
        data = f"{block.index}{block.timestamp}{block.previous_hash}{block.nonce}"
        return hashlib.sha256(data.encode()).hexdigest()

    def _select_quantum_device(self) -> QuantumDevice:
        """Select quantum device based on hashrate"""
        total = sum(d.hashrate_ehs for d in self.quantum_devices)
        rand = random.random() * total
        cumulative = 0
        for device in self.quantum_devices:
            cumulative += device.hashrate_ehs
            if rand <= cumulative:
                return device
        return self.quantum_devices[-1]

    def generate_transactions(self, count: int = None):
        """Generate random transactions"""
        if count is None:
            count = random.randint(5, 20)

        for _ in range(count):
            amount = random.uniform(0.01, 5.0)
            tx = Transaction.create(
                f"user_{random.randint(1, 1000)}",
                f"user_{random.randint(1, 1000)}",
                amount
            )
            self.mempool.add_transaction(tx)

    def mine_block(self):
        """Mine a single block"""
        device = self._select_quantum_device()

        # Select transactions
        selected_txs = sorted(
            self.mempool.pending_txs,
            key=lambda tx: tx.fee_rate,
            reverse=True
        )[:random.randint(500, 2500)]

        total_fees = sum(tx.fee for tx in selected_txs)

        # Calculate reward
        halvings = len(self.chain) // HALVING_INTERVAL
        block_reward = BLOCK_REWARD / (2 ** halvings)
        total_reward = block_reward + total_fees

        # Coinbase transaction
        coinbase = Transaction.create("COINBASE", self.reward_wallet, total_reward, 0)
        all_txs = [coinbase] + selected_txs

        # Calculate block size and weight
        block_size = sum(tx.size_bytes for tx in all_txs)
        block_weight = block_size * 4  # Simplified weight calculation

        # Print mining start
        print(f"\n{'='*80}")
        print(f"⛏️  MINING BLOCK #{len(self.chain)}")
        print(f"{'='*80}")
        print(f"🖥️  Device: {device.device_type}")
        print(f"   ID: {device.device_id}")
        print(f"   Qubits: {device.qubit_count if device.qubit_count > 0 else 'N/A (Classical)'}")
        print(f"   Hashrate: {device.hashrate_ehs:.2f} EH/s ({device.hashrate_ehs * 1_000_000:.0f} TH/s)")
        print(f"   Location: {device.location}")
        print(f"   IP: {device.ip_address}")
        print(f"   Coordinates: {device.latitude:.4f}°N, {abs(device.longitude):.4f}°{'W' if device.longitude < 0 else 'E'}")
        print(f"")
        print(f"📦 Block Info:")
        print(f"   Transactions: {len(selected_txs):,}")
        print(f"   Size: {block_size / 1000:.2f} KB")
        print(f"   Weight: {block_weight:,} WU")
        print(f"   Total Fees: {total_fees:.8f} BTC")
        print(f"   Difficulty: {self.difficulty} leading zeros")

        # Mine
        start_time = time.time()
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=all_txs,
            previous_hash=self.chain[-1].hash,
            nonce=0,
            hash="",
            difficulty=self.difficulty,
            miner=self.reward_wallet,
            reward=total_reward,
            size_bytes=block_size,
            weight=block_weight,
            quantum_device=device
        )

        # Proof of work
        attempts = 0
        while True:
            new_block.nonce = attempts
            new_block.hash = self._calculate_hash(new_block)
            if new_block.hash[:self.difficulty] == "0" * self.difficulty:
                break
            attempts += 1

        mining_time = time.time() - start_time

        print(f"")
        print(f"✅ BLOCK FOUND!")
        print(f"   Hash: {new_block.hash}")
        print(f"   Mining Time: {mining_time:.4f}s")
        print(f"   Nonce: {attempts:,}")
        print(f"   Block Reward: {block_reward:.8f} BTC")
        print(f"   Total Reward: {total_reward:.8f} BTC")
        print(f"")
        print(f"💰 REWARD SENT TO: {self.reward_wallet}")

        # Update state
        self.balances[self.reward_wallet] += total_reward
        self.total_rewards += total_reward
        self.blocks_mined += 1
        self.mempool.remove_transactions(selected_txs)
        self.chain.append(new_block)

        # Simulate block propagation
        self._simulate_block_propagation(new_block)

        # Adjust difficulty
        if len(self.chain) % DIFFICULTY_ADJUSTMENT_INTERVAL == 0:
            self._adjust_difficulty()

        return new_block

    def _simulate_block_propagation(self, block: Block):
        """Simulate block propagation across network"""
        print(f"\n📡 BROADCASTING BLOCK TO NETWORK...")

        propagation_times = []
        for i in range(min(10, self.peer_count)):
            delay = random.uniform(0.01, 0.5)
            propagation_times.append(delay)

        avg_propagation = sum(propagation_times) / len(propagation_times)

        print(f"   Peers notified: {self.peer_count}")
        print(f"   Avg propagation: {avg_propagation*1000:.1f}ms")
        print(f"   Block height: {block.index}")
        print(f"   Status: CONFIRMED ✅")

    def _adjust_difficulty(self):
        """Adjust mining difficulty"""
        if len(self.chain) < DIFFICULTY_ADJUSTMENT_INTERVAL:
            return

        recent = self.chain[-DIFFICULTY_ADJUSTMENT_INTERVAL:]
        time_taken = recent[-1].timestamp - recent[0].timestamp
        expected = TARGET_BLOCK_TIME * DIFFICULTY_ADJUSTMENT_INTERVAL

        ratio = expected / time_taken if time_taken > 0 else 1
        old_diff = self.difficulty

        if ratio < 0.5 and self.difficulty < MAX_DIFFICULTY:
            self.difficulty += 1
            print(f"\n⚡ DIFFICULTY ADJUSTMENT: {old_diff} → {self.difficulty}")
            print(f"   Blocks were mined {1/ratio:.2f}x too fast")
        elif ratio > 2.0 and self.difficulty > 1:
            self.difficulty -= 1
            print(f"\n📉 DIFFICULTY ADJUSTMENT: {old_diff} → {self.difficulty}")
            print(f"   Blocks were mined {ratio:.2f}x too slow")

    def print_network_stats(self):
        """Print network statistics (Mempool-style)"""
        current_hashrate = self.total_hashrate_ehs

        if len(self.chain) > 1:
            recent_time = self.chain[-1].timestamp - self.chain[-10].timestamp if len(self.chain) > 10 else 1
            blocks_per_second = min(10, len(self.chain) - 1) / recent_time if recent_time > 0 else 0
        else:
            blocks_per_second = 0

        print(f"\n{'='*80}")
        print(f"🌐 NETWORK STATISTICS")
        print(f"{'='*80}")
        print(f"Block Height:        {len(self.chain) - 1:,}")
        print(f"Latest Hash:         {self.chain[-1].hash[:32]}...")
        print(f"Difficulty:          {self.difficulty} leading zeros")
        print(f"Network Hashrate:    {current_hashrate:.2f} EH/s ({current_hashrate * 1_000_000:.0f} TH/s)")
        print(f"Blocks/Second:       {blocks_per_second:.4f}")
        print(f"Connected Peers:     {self.peer_count}")
        print(f"")
        print(f"💰 WALLET STATUS:")
        print(f"   Address:          {self.reward_wallet}")
        print(f"   Balance:          {self.balances[self.reward_wallet]:.8f} BTC")
        print(f"   Total Rewards:    {self.total_rewards:.8f} BTC")
        print(f"   Blocks Mined:     {self.blocks_mined:,}")
        print(f"")
        print(f"🌍 MINING DISTRIBUTION:")
        for device in self.quantum_devices:
            percentage = (device.hashrate_ehs / self.total_hashrate_ehs) * 100
            print(f"   {device.country:12} {percentage:5.1f}% - {device.device_type}")
        print(f"{'='*80}")

    def run_infinite(self):
        """Run infinite mining loop"""
        print(f"\n{'='*80}")
        print(f"🔄 STARTING INFINITE MINING LOOP")
        print(f"{'='*80}")
        print(f"Press Ctrl+C to stop")
        print(f"{'='*80}")

        try:
            while True:
                # Generate new transactions
                self.generate_transactions()

                # Show mempool status every 5 blocks
                if self.blocks_mined % 5 == 0:
                    self.mempool.print_mempool_status()

                # Mine block
                self.mine_block()

                # Show network stats every 10 blocks
                if (self.blocks_mined + 1) % 10 == 0:
                    self.print_network_stats()

                # Small delay for readability
                time.sleep(0.1)

        except KeyboardInterrupt:
            print(f"\n\n{'='*80}")
            print(f"⏹️  MINING STOPPED BY USER")
            print(f"{'='*80}")
            self.print_final_stats()

    def print_final_stats(self):
        """Print final mining statistics"""
        print(f"\n{'='*80}")
        print(f"📊 FINAL MINING STATISTICS")
        print(f"{'='*80}")
        print(f"Total Blocks Mined:  {self.blocks_mined:,}")
        print(f"Total BTC Earned:    {self.total_rewards:.8f} BTC")
        print(f"Final Balance:       {self.balances[self.reward_wallet]:.8f} BTC")
        print(f"Wallet Address:      {self.reward_wallet}")
        print(f"Chain Height:        {len(self.chain) - 1:,}")
        print(f"Final Difficulty:    {self.difficulty}")
        print(f"{'='*80}")
        print(f"\n✅ All rewards deposited to: {self.reward_wallet}")
        print()


if __name__ == "__main__":
    print("\n" + "="*80)
    print("⚛️  BITCOIN QUANTUM MINING SIMULATOR - INFINITE LOOP MODE")
    print("="*80)
    print("Realistic Bitcoin mainnet simulation with Mempool-style output")
    print(f"ALL REWARDS → {REWARD_WALLET}")
    print("="*80)
    print()

    miner = InfiniteQuantumMiner(REWARD_WALLET)
    miner.run_infinite()
