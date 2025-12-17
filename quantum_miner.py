#!/usr/bin/env python3
"""
QUANTUM SUPERCOMPUTER BITCOIN MINING SIMULATOR
===============================================

Simulates Bitcoin mining using quantum computing hardware:
- IBM Quantum System One (1,121 qubits)
- Google Sycamore (70 qubits)
- IonQ Aria (25 qubits)
- D-Wave Advantage (5,000+ qubits)
- Classical Supercomputers (exaflop scale)

ALL REWARDS deposited to specified wallet address.

NO REAL BITCOIN. NO REAL QUANTUM COMPUTING. PURELY EDUCATIONAL.
"""

import hashlib
import random
import time
import json
from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict
from datetime import datetime


INITIAL_DIFFICULTY = 4
MAX_DIFFICULTY = 8
DIFFICULTY_ADJUSTMENT_INTERVAL = 10
TARGET_BLOCK_TIME = 1  # Quantum systems mine much faster
BLOCK_REWARD = 6.25
HALVING_INTERVAL = 210000


@dataclass
class QuantumDevice:
    """Quantum computing device specifications"""
    device_id: str
    device_type: str
    manufacturer: str
    qubit_count: int
    gate_fidelity: float
    coherence_time_us: float
    quantum_volume: int
    location: str
    ip_address: str
    hashrate_ehs: float  # Exahashes per second (1 EH/s = 1,000,000 TH/s)

    def __repr__(self):
        return f"{self.device_type} ({self.qubit_count} qubits) - {self.hashrate_ehs} EH/s"


@dataclass
class Transaction:
    txid: str
    from_addr: str
    to_addr: str
    amount: float
    fee: float
    timestamp: float

    @staticmethod
    def create(from_addr: str, to_addr: str, amount: float, fee: float = 0.0001):
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
    quantum_device: QuantumDevice


@dataclass
class RewardRecord:
    """Audit record for quantum mining rewards"""
    timestamp: str
    block_height: int
    block_hash: str
    recipient_address: str
    quantum_device: QuantumDevice
    reward_amount: float
    fee_amount: float
    total_amount: float
    mining_time_seconds: float
    nonce: int
    quantum_advantage: str

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'block_height': self.block_height,
            'block_hash': self.block_hash,
            'recipient': self.recipient_address,
            'device_id': self.quantum_device.device_id,
            'device_type': self.quantum_device.device_type,
            'qubits': self.quantum_device.qubit_count,
            'quantum_volume': self.quantum_device.quantum_volume,
            'hashrate_ehs': self.quantum_device.hashrate_ehs,
            'location': self.quantum_device.location,
            'ip_address': self.quantum_device.ip_address,
            'reward_btc': self.reward_amount,
            'fees_btc': self.fee_amount,
            'total_btc': self.total_amount,
            'mining_time': self.mining_time_seconds,
            'nonce': self.nonce,
            'quantum_advantage': self.quantum_advantage
        }


class QuantumMiningNode:
    """Bitcoin mining node powered by quantum computers"""

    def __init__(self, reward_address: str):
        self.chain: List[Block] = []
        self.mempool: List[Transaction] = []
        self.balances = defaultdict(float)
        self.difficulty = INITIAL_DIFFICULTY
        self.reward_address = reward_address
        self.reward_audit_log: List[RewardRecord] = []
        self.total_rewards_paid = 0.0

        # Create quantum computing devices
        self.quantum_devices = self._initialize_quantum_hardware()

        # Create genesis block
        genesis_tx = Transaction.create("GENESIS", "GENESIS", 0, 0)
        genesis_device = self.quantum_devices[0]
        genesis_block = self._create_genesis_block(genesis_tx, genesis_device)
        self.chain.append(genesis_block)

        print("=" * 80)
        print("⚛️  QUANTUM SUPERCOMPUTER MINING SYSTEM INITIALIZED")
        print("=" * 80)
        print(f"🎯 All rewards will be sent to: {reward_address}")
        print(f"⚛️  Quantum devices: {len(self.quantum_devices)}")
        print(f"🌱 Genesis block: {genesis_block.hash}")
        print(f"💪 Total hashrate: {sum(d.hashrate_ehs for d in self.quantum_devices):.2f} EH/s")
        print("=" * 80)
        print()

    def _initialize_quantum_hardware(self) -> List[QuantumDevice]:
        """Initialize quantum and supercomputer hardware"""
        devices = [
            # IBM Quantum Systems
            QuantumDevice(
                device_id="IBM-Q-SYSTEM-ONE-001",
                device_type="IBM Quantum System One",
                manufacturer="IBM",
                qubit_count=1121,
                gate_fidelity=0.9999,
                coherence_time_us=200,
                quantum_volume=512,
                location="USA, Yorktown Heights, NY",
                ip_address="170.25.142.88",
                hashrate_ehs=45.5
            ),
            QuantumDevice(
                device_id="IBM-Q-HERON-002",
                device_type="IBM Quantum Heron",
                manufacturer="IBM",
                qubit_count=133,
                gate_fidelity=0.9998,
                coherence_time_us=180,
                quantum_volume=256,
                location="USA, Cambridge, MA",
                ip_address="170.25.142.92",
                hashrate_ehs=38.2
            ),
            # Google Quantum
            QuantumDevice(
                device_id="GOOGLE-SYCAMORE-001",
                device_type="Google Sycamore Quantum Processor",
                manufacturer="Google",
                qubit_count=70,
                gate_fidelity=0.9997,
                coherence_time_us=150,
                quantum_volume=128,
                location="USA, Santa Barbara, CA",
                ip_address="172.217.14.228",
                hashrate_ehs=52.8
            ),
            QuantumDevice(
                device_id="GOOGLE-WILLOW-001",
                device_type="Google Willow Quantum Chip",
                manufacturer="Google",
                qubit_count=105,
                gate_fidelity=0.99995,
                coherence_time_us=300,
                quantum_volume=1024,
                location="USA, Santa Barbara, CA",
                ip_address="172.217.14.229",
                hashrate_ehs=125.7
            ),
            # IonQ Systems
            QuantumDevice(
                device_id="IONQ-ARIA-001",
                device_type="IonQ Aria",
                manufacturer="IonQ",
                qubit_count=25,
                gate_fidelity=0.9995,
                coherence_time_us=10000,
                quantum_volume=65536,
                location="USA, College Park, MD",
                ip_address="162.250.191.14",
                hashrate_ehs=89.3
            ),
            # D-Wave Quantum Annealer
            QuantumDevice(
                device_id="DWAVE-ADVANTAGE-001",
                device_type="D-Wave Advantage",
                manufacturer="D-Wave",
                qubit_count=5640,
                gate_fidelity=0.998,
                coherence_time_us=80,
                quantum_volume=64,
                location="Canada, Burnaby, BC",
                ip_address="206.12.94.33",
                hashrate_ehs=215.4
            ),
            # Classical Supercomputers (for comparison)
            QuantumDevice(
                device_id="FRONTIER-EXASCALE-001",
                device_type="Frontier Exascale Supercomputer",
                manufacturer="HPE/AMD",
                qubit_count=0,  # Classical system
                gate_fidelity=1.0,
                coherence_time_us=0,
                quantum_volume=0,
                location="USA, Oak Ridge, TN",
                ip_address="160.91.234.56",
                hashrate_ehs=312.5
            ),
            QuantumDevice(
                device_id="FUGAKU-SUPERCOMPUTER-001",
                device_type="Fugaku Supercomputer",
                manufacturer="Fujitsu",
                qubit_count=0,
                gate_fidelity=1.0,
                coherence_time_us=0,
                quantum_volume=0,
                location="Japan, Kobe",
                ip_address="133.1.138.202",
                hashrate_ehs=278.9
            )
        ]
        return devices

    def _create_genesis_block(self, tx: Transaction, device: QuantumDevice) -> Block:
        """Create genesis block"""
        genesis = Block(
            index=0,
            timestamp=time.time(),
            transactions=[tx],
            previous_hash="0" * 64,
            nonce=0,
            hash="",
            difficulty=self.difficulty,
            miner=self.reward_address,
            reward=0,
            quantum_device=device
        )
        genesis.hash = self._calculate_hash(genesis)
        return genesis

    def _calculate_hash(self, block: Block) -> str:
        """Calculate block hash"""
        block_string = f"{block.index}{block.timestamp}{[tx.txid for tx in block.transactions]}{block.previous_hash}{block.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def _select_quantum_device(self) -> QuantumDevice:
        """Select quantum device based on hashrate"""
        total_hashrate = sum(d.hashrate_ehs for d in self.quantum_devices)
        rand = random.random() * total_hashrate
        cumulative = 0
        for device in self.quantum_devices:
            cumulative += device.hashrate_ehs
            if rand <= cumulative:
                return device
        return self.quantum_devices[-1]

    def mine_block(self) -> Block:
        """Mine a block using quantum hardware"""
        device = self._select_quantum_device()

        # Select transactions from mempool
        selected_txs = sorted(self.mempool, key=lambda tx: tx.fee, reverse=True)[:50]
        total_fees = sum(tx.fee for tx in selected_txs)

        # Calculate block reward
        halvings = len(self.chain) // HALVING_INTERVAL
        block_reward = BLOCK_REWARD / (2 ** halvings)
        total_reward = block_reward + total_fees

        # Create coinbase transaction (ALL rewards to user's wallet)
        coinbase = Transaction.create("COINBASE", self.reward_address, total_reward, 0)
        all_txs = [coinbase] + selected_txs

        print(f"\n⚛️  [{device.device_type}] Mining block {len(self.chain)}...")
        print(f"   Device: {device.device_id}")
        print(f"   Qubits: {device.qubit_count if device.qubit_count > 0 else 'N/A (Classical)'}")
        print(f"   Quantum Volume: {device.quantum_volume if device.quantum_volume > 0 else 'N/A'}")
        print(f"   Hashrate: {device.hashrate_ehs:.2f} EH/s ({device.hashrate_ehs * 1000000:.0f} TH/s)")
        print(f"   Location: {device.location}")
        print(f"   IP: {device.ip_address}")
        print(f"   Transactions: {len(selected_txs)} (fees: {total_fees:.8f} BTC)")
        print(f"   Difficulty: {self.difficulty} leading zeros")

        # Mine the block (quantum speedup simulation)
        start_time = time.time()
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=all_txs,
            previous_hash=self.chain[-1].hash,
            nonce=0,
            hash="",
            difficulty=self.difficulty,
            miner=self.reward_address,
            reward=total_reward,
            quantum_device=device
        )

        # Quantum computers can try exponentially more solutions
        quantum_speedup = device.hashrate_ehs * 10
        attempts = 0
        while True:
            new_block.nonce = attempts
            new_block.hash = self._calculate_hash(new_block)
            if new_block.hash[:self.difficulty] == "0" * self.difficulty:
                break
            attempts += 1

        mining_time = time.time() - start_time

        # Determine quantum advantage
        if device.qubit_count > 0:
            advantage = f"Quantum advantage: {device.qubit_count} qubits, {device.quantum_volume}x volume"
        else:
            advantage = f"Classical exascale performance"

        print(f"✅ Block {new_block.index} mined in {mining_time:.4f}s ({attempts:,} attempts)")
        print(f"   Hash: {new_block.hash}")
        print(f"   Reward: {block_reward:.8f} BTC + {total_fees:.8f} fees")
        print(f"   💰 DEPOSITED TO: {self.reward_address}")
        print(f"   ⚛️  {advantage}")

        # Record reward in audit log
        reward_record = RewardRecord(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            block_height=new_block.index,
            block_hash=new_block.hash,
            recipient_address=self.reward_address,
            quantum_device=device,
            reward_amount=block_reward,
            fee_amount=total_fees,
            total_amount=total_reward,
            mining_time_seconds=mining_time,
            nonce=new_block.nonce,
            quantum_advantage=advantage
        )
        self.reward_audit_log.append(reward_record)
        self.total_rewards_paid += total_reward

        # Update balances
        self.balances[self.reward_address] += total_reward

        # Credit transaction recipients
        for tx in selected_txs:
            if tx.from_addr != "COINBASE":
                self.balances[tx.to_addr] += tx.amount

        # Remove mined transactions
        for tx in selected_txs:
            if tx in self.mempool:
                self.mempool.remove(tx)

        # Add to chain
        self.chain.append(new_block)

        # Adjust difficulty
        if len(self.chain) % DIFFICULTY_ADJUSTMENT_INTERVAL == 0:
            self.adjust_difficulty()

        return new_block

    def adjust_difficulty(self):
        """Adjust mining difficulty"""
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
            print(f"   Quantum systems mining {1/ratio:.2f}x too fast!")
        elif ratio > 2.0 and self.difficulty > 1:
            self.difficulty -= 1
            print(f"\n📉 DIFFICULTY DECREASED: {old_difficulty} → {self.difficulty}")

    def print_status(self):
        """Print current status"""
        print("\n" + "=" * 80)
        print("⚛️  QUANTUM MINING STATUS")
        print("=" * 80)
        print(f"Block Height:      {len(self.chain) - 1}")
        print(f"Latest Hash:       {self.chain[-1].hash[:32]}...")
        print(f"Difficulty:        {self.difficulty} leading zeros")
        print(f"Total Rewards:     {self.total_rewards_paid:.8f} BTC")
        print(f"Wallet Balance:    {self.balances[self.reward_address]:.8f} BTC")
        print(f"Recipient:         {self.reward_address}")
        print(f"Blocks Mined:      {len(self.reward_audit_log)}")
        print("=" * 80)

    def export_audit_log(self, filename: str = "quantum_mining_audit.json"):
        """Export audit log"""
        audit_data = {
            'recipient_wallet': self.reward_address,
            'total_rewards_paid': self.total_rewards_paid,
            'total_blocks_mined': len(self.chain) - 1,
            'total_audit_records': len(self.reward_audit_log),
            'wallet_balance': self.balances[self.reward_address],
            'export_timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'quantum_devices': [
                {
                    'id': d.device_id,
                    'type': d.device_type,
                    'qubits': d.qubit_count,
                    'hashrate_ehs': d.hashrate_ehs
                } for d in self.quantum_devices
            ],
            'records': [record.to_dict() for record in self.reward_audit_log]
        }

        with open(filename, 'w') as f:
            json.dump(audit_data, f, indent=2)

        print(f"\n💾 Audit log exported to {filename}")
        print(f"   Total rewards paid to {self.reward_address}: {self.total_rewards_paid:.8f} BTC")


if __name__ == "__main__":
    # Wallet address containing "78"
    WALLET = "bc1q8z6z78dy5squapjpkeruem98jcezsw37hnae6qjyhxma6jmxyn6qsmqxce"

    print("\n" + "=" * 80)
    print("⚛️  QUANTUM SUPERCOMPUTER BITCOIN MINING SYSTEM")
    print("=" * 80)
    print("Mining using quantum computers and exascale supercomputers")
    print(f"ALL REWARDS deposited to: {WALLET}")
    print("=" * 80)
    print()

    node = QuantumMiningNode(reward_address=WALLET)

    # Mine 20 blocks
    for i in range(20):
        node.mine_block()
        if (i + 1) % 5 == 0:
            node.print_status()

    # Final status
    node.print_status()
    node.export_audit_log()

    print("\n✅ Quantum mining simulation complete!")
    print(f"💰 Total BTC in wallet {WALLET}: {node.balances[WALLET]:.8f}")
