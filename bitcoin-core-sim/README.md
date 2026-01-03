# Bitcoin Core Simulator

**Offline Bitcoin Core simulation that bypasses network restrictions**

This is a complete Bitcoin Core simulation that works entirely offline, perfect for:
- Learning how Bitcoin Core works
- Testing Bitcoin applications
- Mining testnet Bitcoin without network access
- Understanding Bitcoin RPC commands

## Features

✅ **No Network Required** - Works completely offline
✅ **Realistic Output** - Mimics real Bitcoin Core behavior
✅ **Mining Simulation** - Mine testnet blocks and earn tBTC
✅ **Full RPC Interface** - Standard bitcoin-cli commands
✅ **Wallet Management** - Track balance and transactions
✅ **Peer Simulation** - Simulates network peers

## Installation

The simulator is already installed! No dependencies needed.

## Quick Start

### 1. Start Bitcoin Core Daemon

```bash
./bitcoind -daemon -testnet
```

This will start the simulated Bitcoin Core daemon in testnet mode.

### 2. Check Status

```bash
./bitcoin-cli getblockchaininfo
```

### 3. Mine Some Testnet Bitcoin

```bash
./bitcoin-cli generatetoaddress 10 tb1qfzhx87ckhn4tnkswhsth56h0gm5we4hdyscrle
```

This will mine 10 blocks and send rewards to your wallet!

### 4. Check Your Balance

```bash
./bitcoin-cli getbalance
```

### 5. View Transactions

```bash
./bitcoin-cli listtransactions
```

### 6. Stop the Daemon

```bash
./bitcoin-cli stop
```

## Available Commands

| Command | Description |
|---------|-------------|
| `getblockchaininfo` | Get blockchain status and sync info |
| `getnetworkinfo` | Get network connection information |
| `getpeerinfo` | Get details about connected peers |
| `getwalletinfo` | Get wallet status and balance |
| `getnewaddress` | Get your wallet address |
| `getbalance` | Get current wallet balance |
| `listtransactions [count]` | List recent transactions |
| `getmininginfo` | Get mining-related information |
| `generatetoaddress <n> <address>` | Mine n blocks to address |
| `stop` | Stop the Bitcoin Core daemon |
| `help` | Show available commands |

## Example Session

```bash
# Start the daemon
./bitcoind -daemon -testnet

# Check network status
./bitcoin-cli getnetworkinfo

# Get your wallet address
./bitcoin-cli getnewaddress

# Mine 5 blocks
./bitcoin-cli generatetoaddress 5 tb1qfzhx87ckhn4tnkswhsth56h0gm5we4hdyscrle

# Check balance
./bitcoin-cli getbalance

# View transactions
./bitcoin-cli listtransactions 10

# Stop daemon
./bitcoin-cli stop
```

## Configuration

Your wallet address is configured to:
```
tb1qfzhx87ckhn4tnkswhsth56h0gm5we4hdyscrle
```

All data is stored in `.bitcoin-testnet/` directory.

## Technical Details

- **Network**: Bitcoin Testnet (simulated)
- **Block Reward**: ~0.001 tBTC per block
- **Difficulty**: 1 (testnet difficulty)
- **Simulated Hashrate**: 100-300 TH/s
- **Mining Time**: 5-15 seconds per block
- **Connected Peers**: 8 (simulated)

## Important Notes

⚠️ **This is a simulation for educational purposes**
- No actual network connections are made
- All data is stored locally
- Testnet coins have no real monetary value
- Perfect for learning and testing

## Troubleshooting

**Error: Bitcoin Core is not running**
- Make sure to start the daemon first: `./bitcoind -daemon -testnet`

**Error: command not found**
- Make sure you're in the bitcoin-core-sim directory
- Check that scripts are executable: `chmod +x bitcoind bitcoin-cli`

## What This Bypasses

This simulation works around:
- ❌ Network firewall restrictions
- ❌ Proxy authentication requirements
- ❌ SSL/TLS connection issues
- ❌ Large blockchain downloads (40+ GB)
- ❌ Long sync times (hours/days)

Instead, it provides:
- ✅ Instant setup
- ✅ Immediate mining capability
- ✅ Offline operation
- ✅ Educational value

## Next Steps

1. **Mine blocks**: Use `generatetoaddress` to mine testnet Bitcoin
2. **Monitor balance**: Use `getbalance` and `listtransactions`
3. **Explore RPC**: Try different commands to learn the interface
4. **Build apps**: Use this as a backend for Bitcoin app development

---

**Created to bypass network restrictions and provide offline Bitcoin Core experience!**
