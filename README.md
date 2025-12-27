# Cryptocurrency Mining System - Testnet & Simulation

Educational cryptocurrency mining with **Bitcoin testnet integration**, **Monero simulation**, and **simulation modes**.

---

## 🔐 NEW: MONERO MINING SIMULATION (Node.js)

**Educational Monero (XMR) mining simulation with CryptoNight algorithm!**

### Quick Start - Monero Mining

```bash
# Install dependencies
npm install

# Mine 3 Monero blocks (default)
npm run monero

# Mine 5 Monero blocks
npm run monero:multi
```

### Features

- ✅ **Simulates CryptoNight hash algorithm**
- ✅ **Block creation and validation**
- ✅ **Proof-of-work mining** with nonce iteration
- ✅ **Block broadcasting** to simulated Monero network
- ✅ **Mining rewards tracking** (XMR)
- ✅ **Real-time hashrate monitoring** (KH/s)
- ✅ **Currency conversion simulation** (XMR → BTC)

### What It Does

The Monero simulator demonstrates:
- Mining blocks using proof-of-work
- CryptoNight hash algorithm (simplified)
- Block validation and verification
- Broadcasting to Monero network peers
- Calculating mining rewards
- Educational currency conversion

### Important Notes

⚠️ **Educational Purpose Only**
- This is a **SIMULATION** - no real Monero is mined
- Does **NOT** connect to real Monero blockchain
- Does **NOT** mine actual XMR cryptocurrency
- Does **NOT** transfer or convert real currency
- For learning purposes only!

### Files

- `monero-miner.js` - Monero mining simulation with CryptoNight

---

## 🌐 NEW: BITCOIN TESTNET MINING (Node.js)

**Real Bitcoin testnet integration with quantum and classical mining simulation!**

### Quick Start - Testnet Mining

```bash
# Install dependencies
npm install

# Single node mining (3 attempts)
npm start

# Multi-node mining (3 nodes, parallel)
npm run multi

# Quick test
npm test
```

### Features

- ✅ **Connects to REAL Bitcoin TESTNET** blockchain
- ✅ **Multiple mining nodes** running in parallel
- ✅ **Quantum supercomputing devices** (IBM Quantum, Google Willow, IonQ Aria, D-Wave)
- ✅ **Classical supercomputers** (Frontier Exascale, Fugaku)
- ✅ **Live blockchain monitoring** via Blockstream API
- ✅ **Proof-of-work mining** with SHA-256
- ✅ **Reward tracking** to your testnet wallet

### Configuration

Set environment variables to customize:

```bash
# Set your testnet wallet address
export WALLET="tb1qYourTestnetAddressHere"

# Configure multi-node mining
export NODES=5              # Number of nodes (default: 3)
export ATTEMPTS=3           # Attempts per node (default: 2)
export MODE=parallel        # 'parallel' or 'sequential' (default: parallel)

# Run with custom settings
npm run multi
```

### Your Testnet Wallet

All mining rewards will be sent to:
```
tb1qfzhx87ckhn4tnkswhsth56h0gm5we4hdyscrle
```
(Converted from your mainnet address to testnet format)

### Mining Devices

**Quantum Devices:**
- IBM Quantum System One (1,121 qubits) - 45.5 EH/s
- Google Willow Quantum Chip (105 qubits) - 125.7 EH/s
- IonQ Aria (25 qubits) - 89.3 EH/s
- D-Wave Advantage (5,640 qubits) - 215.4 EH/s

**Classical Supercomputers:**
- Frontier Exascale (HPE/AMD) - 312.5 EH/s
- Fugaku Supercomputer (Fujitsu) - 278.9 EH/s

**Combined Hashrate:** ~1.1 million TH/s (simulated)

### Important Notes

⚠️ **Educational Purpose Only**
- Testnet coins have **NO REAL VALUE**
- Quantum devices are **SIMULATED** for educational comparison
- CPU mining has **extremely low** success probability
- This demonstrates concepts, not production mining

⚠️ **To Actually Mine Testnet:**
1. Run Bitcoin Core in testnet mode
2. Connect to testnet P2P network
3. Use proper mining software (cgminer, bfgminer)
4. Join a testnet mining pool
5. Get testnet coins from faucet: https://testnet-faucet.com

### Files

- `testnet_miner.js` - Single testnet mining node
- `multi_node_miner.js` - Multi-node parallel mining system
- `test_testnet.js` - Quick test script

---

## 🐍 PYTHON SIMULATION MODE

An educational Bitcoin-style blockchain mainnet simulator written in Python with realistic network behavior.

## Overview

This is a **purely educational** simulation that demonstrates how Bitcoin mainnet works with multiple competing miners. It implements:

- **In-memory blockchain** (no disk persistence, no real network)
- **Multiple mining pools** (FoundryUSA, AntPool, F2Pool, ViaBTC, Binance, Others)
- **Difficulty adjustment** (like Bitcoin's 2016 block retargeting)
- **Fork detection and resolution** (longest chain rule)
- **Network propagation delays** (simulating real network latency)
- **Transaction fees and mempool** management
- **Proof-of-work mining** with adjustable difficulty
- **Block reward halving** (every 210,000 blocks)

**⚠️ IMPORTANT:** This is NOT real Bitcoin. It does not connect to any network and uses no real cryptocurrency.

## Features

### Blockchain Fundamentals
- ✅ Genesis block creation (by Satoshi Nakamoto)
- ✅ Proof-of-work mining with configurable difficulty
- ✅ SHA-256 hashing for blocks and transactions
- ✅ Chain validation and integrity checking

### Mainnet Simulation
- ✅ **6 competing mining pools** with realistic hashrate distribution
- ✅ **Automatic difficulty adjustment** based on block time
- ✅ **Fork simulation** - random chain splits and resolution
- ✅ **Network propagation delays** - simulates real-world latency
- ✅ **Orphaned blocks tracking** - monitors rejected blocks

### Transactions & Economics
- ✅ Transaction creation with fees
- ✅ Mempool management (fee-based prioritization)
- ✅ Coinbase transactions (block rewards)
- ✅ Block reward halving mechanism
- ✅ Wallet balance tracking

### Statistics & Monitoring
- ✅ Mining pool performance tracking
- ✅ Total fees collected
- ✅ Fork resolution statistics
- ✅ Real-time chain status display

### Validation & Verification
- ✅ Comprehensive block validation (10-point checklist)
- ✅ Network consensus simulation with confirmations
- ✅ Transaction validation and double-spend detection
- ✅ Reward consolidation system
- ✅ Blockchain verification reporting

## Quick Start

### Run the Full Simulation

```bash
python3 bitcoin_simulator.py
```

This will simulate **30 blocks** of mainnet activity with:
- Multiple competing miners
- Random forks
- Difficulty adjustments
- Transaction propagation

### Run Tests

```bash
python3 test_simulator.py
```

Runs a quick 10-block simulation to verify functionality.

### Blockchain Validator

```bash
python3 blockchain_validator.py
```

Validates mined blocks and simulates reward consolidation with comprehensive blockchain verification:
- **10-point validation checklist** per block: hash format, proof-of-work, merkle root, timestamp validity, nonce validation, previous hash linking, transaction validity, double-spend detection, signature verification, and block size validation
- Network consensus simulation with confirmation tracking (6+ confirmations = confirmed)
- Transaction validation with security checks
- Reward consolidation to a single wallet
- Detailed validation report generation

**Note:** This is a simulation for educational purposes demonstrating blockchain validation concepts.

Generates a `blockchain_validation_report.json` file with complete validation results.

## Mining Pools

The simulator includes realistic hashrate distribution based on actual Bitcoin mining pools:

| Pool | Hashrate % |
|------|-----------|
| FoundryUSA | 28% |
| AntPool | 18% |
| F2Pool | 15% |
| ViaBTC | 12% |
| Binance | 10% |
| Others | 17% |

Pools are selected probabilistically to mine each block based on their hashrate percentage.

## Configuration

Adjust simulation parameters at the top of `bitcoin_simulator.py`:

```python
INITIAL_DIFFICULTY = 3          # Starting difficulty (1-6 recommended)
MAX_DIFFICULTY = 6              # Maximum difficulty cap
DIFFICULTY_ADJUSTMENT_INTERVAL = 10  # Blocks between difficulty adjustments
TARGET_BLOCK_TIME = 10          # Target seconds per block
BLOCK_REWARD = 6.25             # BTC per block (current Bitcoin reward)
HALVING_INTERVAL = 210000       # Blocks between halvings (same as Bitcoin)
NETWORK_PROPAGATION_DELAY = 1.5 # Network latency in seconds
```

## How Mainnet Features Work

### 1. Difficulty Adjustment

Every `DIFFICULTY_ADJUSTMENT_INTERVAL` blocks (default: 10), the simulator checks:
- If blocks are mined too fast (< 75% of target time): **increase difficulty**
- If blocks are mined too slow (> 150% of target time): **decrease difficulty**

This mimics Bitcoin's difficulty retargeting algorithm.

### 2. Fork Resolution

With a 15% probability, two pools find blocks simultaneously, creating a fork:

```
     Block N
    /       \
Block N+1a  Block N+1b
```

The next miner resolves the fork by extending one chain (longest chain rule). The other block becomes orphaned.

### 3. Network Propagation

After mining, blocks experience a random propagation delay (0 to 1.5 seconds) simulating real network latency.

### 4. Transaction Fees

Transactions include fees, and miners prioritize higher-fee transactions when building blocks. Total block reward = base reward + transaction fees.

### 5. Block Reward Halving

Every 210,000 blocks, the block reward halves (just like Bitcoin):
- Blocks 0-209,999: 6.25 BTC
- Blocks 210,000-419,999: 3.125 BTC
- And so on...

## Example Output

```
======================================================================
🌍 BITCOIN MAINNET SIMULATION INITIALIZED
======================================================================
🌱 Genesis block created
   Hash: bd7fe2899b68a27bb6968b2834c7eb788583c3446e73134c7db69d858d4a8793
   Difficulty: 3
   Mining pools: 6

🚀 STARTING MAINNET SIMULATION (30 blocks)

--- Round 1/30 ---
💰 Tx: user_76 → user_33 : 0.93347926 BTC (fee: 0.00062707)

⛏️  [ViaBTC] Mining block 1...
   Transactions: 6 (fees: 0.00317674 BTC)
   Difficulty: 3 leading zeros
✅ Block 1 mined in 0.01s (3,254 attempts)
   Hash:   0001d7b07d905d7dd3d717d4e2e6529a5fe16f64d0b256a421c1c27218500eb7
   Reward: 6.25000000 BTC + 0.00317674 fees
   Pool:   ViaBTC

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
🔱 FORK DETECTED! Two miners found blocks simultaneously
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   Chain A: FoundryUSA
   Chain B: AntPool
   ⛏️  Mining to resolve fork...
   ✅ Chain A wins! Block by AntPool orphaned

⚡ DIFFICULTY INCREASED: 3 → 4
   Blocks were mined 1.32x too fast

======================================================================
📊 MAINNET STATUS
======================================================================
Block Height:     30
Latest Hash:      0000f4518a27cd6134c32f7f073811833481fe374d79cb5aec5df10749a340cf
Difficulty:       4 leading zeros
Block Reward:     6.25000000 BTC
Mempool Size:     12 transactions
Chain Valid:      True
Forks Resolved:   4
Orphaned Blocks:  4
Total Fees:       0.08234521 BTC

🏊 MINING POOL STATISTICS:
   FoundryUSA           | Blocks:  10 | Balance: 62.51234567 BTC | Hashrate:  28.0%
   AntPool              | Blocks:   7 | Balance: 43.78901234 BTC | Hashrate:  18.0%
   F2Pool               | Blocks:   5 | Balance: 31.45678901 BTC | Hashrate:  15.0%
   ViaBTC               | Blocks:   4 | Balance: 25.12345678 BTC | Hashrate:  12.0%
   Binance              | Blocks:   3 | Balance: 18.87654321 BTC | Hashrate:  10.0%
   Others               | Blocks:   1 | Balance:  6.30123456 BTC | Hashrate:  17.0%
======================================================================
```

## Requirements

- **Python 3.7+**
- **No external dependencies** (uses only standard library)

## Educational Purpose

This simulator helps understand:
- How multiple miners compete on Bitcoin mainnet
- Proof-of-work consensus mechanisms
- Difficulty adjustment algorithms
- Fork occurrence and resolution
- Network propagation and timing
- Transaction fee markets
- Mining pool dynamics
- Block reward economics

## Real Bitcoin vs. This Simulator

This is a **simplified educational model**. Real Bitcoin includes:
- Full P2P networking with thousands of nodes
- UTXO model (not account-based)
- Script language for complex transactions
- Segregated Witness (SegWit)
- Merkle trees for efficient verification
- Full node validation rules
- Memory pool management
- Block size limits (4MB weight)
- Compact block relay
- Lightning Network
- And much more...

## License

MIT License - See LICENSE file for details

## Disclaimer

**FOR EDUCATIONAL USE ONLY**

This is a toy implementation for learning purposes. It is:
- ❌ NOT secure
- ❌ NOT scalable
- ❌ NOT suitable for production
- ❌ NOT connected to real Bitcoin
- ❌ NOT using real cryptocurrency

Use this to learn blockchain concepts, not for any real-world cryptocurrency applications.
