#!/usr/bin/env python3
"""
BITCOIN MAINNET SIMULATOR WITH REWARD TRACKING & SECURITY AUDIT
================================================================

Enhanced simulation with comprehensive tracking:
- Device IDs and hardware fingerprints
- IP addresses and geographic locations
- Full audit trail of all reward payments
- Timestamp tracking for all transactions
- Mining equipment specifications
- Security monitoring and alerts

NO REAL BITCOIN. NO REAL NETWORK. PURELY EDUCATIONAL.
"""

import hashlib
import random
import time
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from collections import defaultdict
from datetime import datetime

# Mainnet-style configuration
INITIAL_DIFFICULTY = 3
MAX_DIFFICULTY = 6
DIFFICULTY_ADJUSTMENT_INTERVAL = 10
TARGET_BLOCK_TIME = 10
BLOCK_REWARD = 6.25
HALVING_INTERVAL = 210000
NETWORK_PROPAGATION_DELAY = 1.5


@dataclass
class DeviceInfo:
    """Tracks device/miner information"""
    device_id: str
    ip_address: str
    location: str
    hardware_type: str
    asic_model: str
    hashrate_ths: float  # Terahashes per second
    firmware_version: str

    def __repr__(self):
        return f"{self.device_id} ({self.ip_address}) @ {self.location}"


@dataclass
class RewardRecord:
    """Audit record for each reward payment"""
    timestamp: str
    block_height: int
    block_hash: str
    recipient_address: str
    device_info: DeviceInfo
    reward_amount: float
    fee_amount: float
    total_amount: float
    transaction_count: int
    mining_time_seconds: float
    nonce: int

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'block_height': self.block_height,
            'block_hash': self.block_hash,
            'recipient': self.recipient_address,
            'device_id': self.device_info.device_id,
            'ip_address': self.device_info.ip_address,
            'location': self.device_info.location,
            'hardware': self.device_info.asic_model,
            'reward_btc': self.reward_amount,
            'fees_btc': self.fee_amount,
            'total_btc': self.total_amount,
            'transactions': self.transaction_count,
            'mining_time': self.mining_time_seconds,
            'nonce': self.nonce
        }


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
            timestamp=now
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


class MiningPool:
    """Represents a mining pool with device tracking"""

    def __init__(self, name: str, address: str, hashrate_percent: float,
                 location: str, ip_base: str):
        self.name = name
        self.address = address
        self.hashrate_percent = hashrate_percent
        self.location = location
        self.ip_base = ip_base

        # Generate multiple mining devices for this pool
        self.devices = self._generate_devices()
        self.current_device_index = 0

    def _generate_devices(self) -> List[DeviceInfo]:
        """Generate realistic mining devices for this pool"""
        num_devices = random.randint(3, 8)
        devices = []

        asic_models = [
            ("Antminer S19 Pro", 110.0),
            ("Antminer S19j Pro", 104.0),
            ("Whatsminer M50S", 126.0),
            ("Whatsminer M30S++", 112.0),
            ("AvalonMiner 1246", 90.0),
            ("Antminer S21", 200.0)
        ]

        for i in range(num_devices):
            asic_model, hashrate = random.choice(asic_models)
            device = DeviceInfo(
                device_id=f"{self.name}-ASIC-{i+1:03d}-{random.randint(10000, 99999)}",
                ip_address=f"{self.ip_base}.{random.randint(1, 254)}",
                location=self.location,
                hardware_type="ASIC Miner",
                asic_model=asic_model,
                hashrate_ths=hashrate,
                firmware_version=f"v{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 20)}"
            )
            devices.append(device)

        return devices

    def get_random_device(self) -> DeviceInfo:
        """Get a random device from this pool"""
        return random.choice(self.devices)

    def get_next_device(self) -> DeviceInfo:
        """Get next device in round-robin fashion"""
        device = self.devices[self.current_device_index]
        self.current_device_index = (self.current_device_index + 1) % len(self.devices)
        return device


class TrackedMainnetNode:
    """Enhanced mainnet node with full reward tracking"""

    def __init__(self):
        self.chain: List[Block] = []
        self.mempool: List[Transaction] = []
        self.balances = defaultdict(float)
        self.difficulty = INITIAL_DIFFICULTY
        self.orphaned_blocks: List[Block] = []
        self.forks_resolved = 0

        # Reward tracking
        self.reward_audit_log: List[RewardRecord] = []
        self.total_rewards_paid = 0.0

        # Create mining pools with device tracking
        self.pools = [
            MiningPool("FoundryUSA", "FoundryUSA", 28.0, "USA, New York", "45.23.156"),
            MiningPool("AntPool", "AntPool", 18.0, "China, Beijing", "202.108.22"),
            MiningPool("F2Pool", "F2Pool", 15.0, "China, Shanghai", "115.239.210"),
            MiningPool("ViaBTC", "ViaBTC", 12.0, "China, Shenzhen", "119.29.29"),
            MiningPool("Binance", "Binance", 10.0, "Singapore", "103.253.145"),
            MiningPool("Others", "Others", 17.0, "Global, Distributed", "185.220.101")
        ]

        # Create genesis block
        genesis_tx = Transaction.create("GENESIS", "GENESIS", 0, 0)
        genesis_block = self._create_genesis_block(genesis_tx)
        self.chain.append(genesis_block)

        print("=" * 70)
        print("🔒 TRACKED BITCOIN MAINNET SIMULATION INITIALIZED")
        print("=" * 70)
        print("🌱 Genesis block created")
        print(f"   Hash: {genesis_block.hash}")
        print(f"   Difficulty: {self.difficulty}")
        print(f"   Mining pools: {len(self.pools)}")
        print(f"   Total devices: {sum(len(p.devices) for p in self.pools)}")
        print()

    def _create_genesis_block(self, tx: Transaction) -> Block:
        """Create the genesis block"""
        genesis = Block(
            index=0,
            timestamp=time.time(),
            transactions=[tx],
            previous_hash="0" * 64,
            nonce=0,
            hash="",
            difficulty=self.difficulty,
            miner="GENESIS",
            reward=0
        )
        genesis.hash = self._calculate_hash(genesis)
        return genesis

    def _calculate_hash(self, block: Block) -> str:
        """Calculate block hash"""
        block_string = f"{block.index}{block.timestamp}{[tx.txid for tx in block.transactions]}{block.previous_hash}{block.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def _select_mining_pool(self) -> MiningPool:
        """Select a mining pool based on hashrate distribution"""
        rand = random.random() * 100
        cumulative = 0
        for pool in self.pools:
            cumulative += pool.hashrate_percent
            if rand <= cumulative:
                return pool
        return self.pools[-1]

    def mine_block(self) -> Optional[Block]:
        """Mine a new block with full device tracking"""
        pool = self._select_mining_pool()
        device = pool.get_random_device()

        # Select transactions
        selected_txs = sorted(self.mempool, key=lambda tx: tx.fee, reverse=True)[:10]
        total_fees = sum(tx.fee for tx in selected_txs)

        # Calculate block reward (with halving)
        halvings = len(self.chain) // HALVING_INTERVAL
        block_reward = BLOCK_REWARD / (2 ** halvings)
        total_reward = block_reward + total_fees

        # Create coinbase transaction
        coinbase = Transaction.create("COINBASE", pool.address, total_reward, 0)
        all_txs = [coinbase] + selected_txs

        print(f"\n⛏️  [{pool.name}] Mining block {len(self.chain)}...")
        print(f"   Device: {device.device_id}")
        print(f"   IP: {device.ip_address} ({device.location})")
        print(f"   Hardware: {device.asic_model} ({device.hashrate_ths} TH/s)")
        print(f"   Transactions: {len(selected_txs)} (fees: {total_fees:.8f} BTC)")
        print(f"   Difficulty: {self.difficulty} leading zeros")

        # Mine the block
        start_time = time.time()
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=all_txs,
            previous_hash=self.chain[-1].hash,
            nonce=0,
            hash="",
            difficulty=self.difficulty,
            miner=pool.address,
            reward=total_reward
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

        print(f"✅ Block {new_block.index} mined in {mining_time:.2f}s ({attempts:,} attempts)")
        print(f"   Hash:   {new_block.hash}")
        print(f"   Reward: {block_reward:.8f} BTC + {total_fees:.8f} fees")
        print(f"   Pool:   {pool.name}")

        # Record reward in audit log
        reward_record = RewardRecord(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            block_height=new_block.index,
            block_hash=new_block.hash,
            recipient_address=pool.address,
            device_info=device,
            reward_amount=block_reward,
            fee_amount=total_fees,
            total_amount=total_reward,
            transaction_count=len(selected_txs),
            mining_time_seconds=mining_time,
            nonce=new_block.nonce
        )
        self.reward_audit_log.append(reward_record)
        self.total_rewards_paid += total_reward

        # Update balances
        self.balances[pool.address] += total_reward

        # Credit transaction recipients
        for tx in selected_txs:
            if tx.from_addr != "COINBASE":
                self.balances[tx.to_addr] += tx.amount

        # Remove mined transactions from mempool
        for tx in selected_txs:
            if tx in self.mempool:
                self.mempool.remove(tx)

        # Add block to chain
        self.chain.append(new_block)

        # Adjust difficulty if needed
        if len(self.chain) % DIFFICULTY_ADJUSTMENT_INTERVAL == 0:
            self.adjust_difficulty()

        return new_block

    def adjust_difficulty(self):
        """Adjust mining difficulty based on block times"""
        if len(self.chain) < DIFFICULTY_ADJUSTMENT_INTERVAL:
            return

        recent_blocks = self.chain[-DIFFICULTY_ADJUSTMENT_INTERVAL:]
        time_taken = recent_blocks[-1].timestamp - recent_blocks[0].timestamp
        expected_time = TARGET_BLOCK_TIME * DIFFICULTY_ADJUSTMENT_INTERVAL

        ratio = expected_time / time_taken if time_taken > 0 else 1

        old_difficulty = self.difficulty

        if ratio < 0.5 and self.difficulty < MAX_DIFFICULTY:
            self.difficulty += 1
            print(f"\n⚡ DIFFICULTY INCREASED: {old_difficulty} → {self.difficulty}")
            print(f"   Blocks were mined {1/ratio:.2f}x too fast")
        elif ratio > 2.0 and self.difficulty > 1:
            self.difficulty -= 1
            print(f"\n📉 DIFFICULTY DECREASED: {old_difficulty} → {self.difficulty}")
            print(f"   Blocks were mined {ratio:.2f}x too slow")

    def print_reward_audit(self, last_n: int = 10):
        """Print detailed reward audit log"""
        print("\n" + "=" * 70)
        print(f"🔍 REWARD AUDIT LOG (Last {min(last_n, len(self.reward_audit_log))} records)")
        print("=" * 70)

        for record in self.reward_audit_log[-last_n:]:
            print(f"\n📦 Block #{record.block_height} - {record.timestamp}")
            print(f"   Hash: {record.block_hash[:32]}...")
            print(f"   Recipient: {record.recipient_address}")
            print(f"   Device ID: {record.device_info.device_id}")
            print(f"   IP Address: {record.device_info.ip_address}")
            print(f"   Location: {record.device_info.location}")
            print(f"   Hardware: {record.device_info.asic_model} ({record.device_info.hashrate_ths} TH/s)")
            print(f"   Reward: {record.reward_amount:.8f} BTC")
            print(f"   Fees: {record.fee_amount:.8f} BTC")
            print(f"   Total: {record.total_amount:.8f} BTC")
            print(f"   Mining Time: {record.mining_time_seconds:.2f}s ({record.nonce:,} attempts)")

        print("\n" + "=" * 70)
        print(f"💰 TOTAL REWARDS PAID: {self.total_rewards_paid:.8f} BTC")
        print(f"📝 TOTAL AUDIT RECORDS: {len(self.reward_audit_log)}")
        print("=" * 70)

    def export_audit_log(self, filename: str = "reward_audit.json"):
        """Export full audit log to JSON file"""
        audit_data = {
            'total_rewards_paid': self.total_rewards_paid,
            'total_blocks': len(self.chain),
            'total_records': len(self.reward_audit_log),
            'export_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'records': [record.to_dict() for record in self.reward_audit_log]
        }

        with open(filename, 'w') as f:
            json.dump(audit_data, f, indent=2)

        print(f"\n💾 Audit log exported to {filename}")
        print(f"   Total records: {len(self.reward_audit_log)}")
        print(f"   Total rewards: {self.total_rewards_paid:.8f} BTC")

    def add_transaction(self, from_addr: str, to_addr: str, amount: float, fee: float = 0.0001) -> bool:
        """Add a transaction to the mempool"""
        if from_addr != "COINBASE" and self.balances[from_addr] < amount + fee:
            return False

        tx = Transaction.create(from_addr, to_addr, amount, fee)
        self.mempool.append(tx)

        if from_addr != "COINBASE":
            self.balances[from_addr] -= (amount + fee)

        return True

    @property
    def chain_height(self) -> int:
        return len(self.chain) - 1


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🔒 BITCOIN MAINNET SIMULATOR WITH REWARD TRACKING")
    print("=" * 70)
    print("This simulator tracks all reward payments with:")
    print("  • Device IDs and hardware specifications")
    print("  • IP addresses and geographic locations")
    print("  • Complete audit trail with timestamps")
    print("  • Mining performance metrics")
    print("=" * 70)
    print()

    node = TrackedMainnetNode()

    # Mine 5 blocks
    for i in range(5):
        print(f"\n{'='*70}")
        print(f"MINING BLOCK #{i+1}")
        print('='*70)
        node.mine_block()

    # Print reward audit
    node.print_reward_audit()

    # Export to JSON
    node.export_audit_log()

    print("\n✅ Simulation complete!")
