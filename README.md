# Bitcoin Mainnet Simulator

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
