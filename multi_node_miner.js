#!/usr/bin/env node

/**
 * MULTI-NODE BITCOIN TESTNET MINING SYSTEM
 * =========================================
 *
 * Runs MULTIPLE Bitcoin testnet mining nodes simultaneously.
 * Each node competes to find blocks using quantum and classical miners.
 *
 * Features:
 * - Multiple parallel mining instances
 * - Quantum supercomputing devices (simulated)
 * - Classical supercomputing devices
 * - Real testnet blockchain monitoring
 * - Consolidated reward tracking
 */

const TestnetMiner = require('./testnet_miner');

class MultiNodeManager {
    constructor(walletAddress, numNodes = 3) {
        this.walletAddress = walletAddress;
        this.numNodes = numNodes;
        this.miners = [];
        this.globalStats = {
            totalAttempts: 0,
            totalBlocksFound: 0,
            totalHashes: 0,
            startTime: Date.now()
        };
    }

    /**
     * Initialize all mining nodes
     */
    initializeNodes() {
        console.log(`\n${'='.repeat(80)}`);
        console.log(`🌐 MULTI-NODE BITCOIN TESTNET MINING SYSTEM`);
        console.log(`${'='.repeat(80)}`);
        console.log(`Initializing ${this.numNodes} mining nodes...`);
        console.log(`Wallet Address: ${this.walletAddress}`);
        console.log(`Network: Bitcoin TESTNET`);
        console.log(`${'='.repeat(80)}`);

        for (let i = 0; i < this.numNodes; i++) {
            const minerId = `quantum-node-${i + 1}`;
            const miner = new TestnetMiner(this.walletAddress, minerId);
            this.miners.push(miner);
            console.log(`✅ Node ${i + 1} initialized: ${minerId}`);
        }

        console.log(`\n✅ All ${this.numNodes} nodes initialized successfully!`);
    }

    /**
     * Run all nodes in parallel
     */
    async startAllNodes(attemptsPerNode = 2) {
        console.log(`\n${'='.repeat(80)}`);
        console.log(`🚀 STARTING MULTI-NODE MINING SESSION`);
        console.log(`${'='.repeat(80)}`);
        console.log(`Active Nodes: ${this.numNodes}`);
        console.log(`Attempts per node: ${attemptsPerNode}`);
        console.log(`Total attempts: ${this.numNodes * attemptsPerNode}`);
        console.log(`${'='.repeat(80)}\n`);

        // Create mining promises for all nodes
        const miningPromises = this.miners.map((miner, index) => {
            return new Promise(async (resolve) => {
                console.log(`\n🔄 Starting ${miner.minerId}...`);

                try {
                    await miner.startMining(attemptsPerNode);
                    resolve({
                        minerId: miner.minerId,
                        stats: miner.miningStats
                    });
                } catch (error) {
                    console.error(`❌ Error in ${miner.minerId}:`, error.message);
                    resolve({
                        minerId: miner.minerId,
                        stats: miner.miningStats,
                        error: error.message
                    });
                }
            });
        });

        // Wait for all nodes to complete
        console.log(`\n⏳ All nodes are now mining in parallel...\n`);
        const results = await Promise.all(miningPromises);

        // Aggregate results
        this.aggregateResults(results);
    }

    /**
     * Aggregate results from all nodes
     */
    aggregateResults(results) {
        console.log(`\n${'='.repeat(80)}`);
        console.log(`📊 MULTI-NODE MINING RESULTS`);
        console.log(`${'='.repeat(80)}`);

        let totalAttempts = 0;
        let totalBlocksFound = 0;
        let totalHashes = 0;

        results.forEach((result, index) => {
            console.log(`\n🖥️  Node ${index + 1}: ${result.minerId}`);
            console.log(`   Attempts: ${result.stats.attempts}`);
            console.log(`   Blocks Found: ${result.stats.blocksFound}`);
            console.log(`   Hashes: ${result.stats.hashesComputed.toLocaleString()}`);

            totalAttempts += result.stats.attempts;
            totalBlocksFound += result.stats.blocksFound;
            totalHashes += result.stats.hashesComputed;

            if (result.error) {
                console.log(`   ⚠️  Error: ${result.error}`);
            }
        });

        const runtime = (Date.now() - this.globalStats.startTime) / 1000;
        const avgHashrate = Math.floor(totalHashes / runtime);

        console.log(`\n${'='.repeat(80)}`);
        console.log(`🏆 CONSOLIDATED STATISTICS`);
        console.log(`${'='.repeat(80)}`);
        console.log(`Total Nodes: ${this.numNodes}`);
        console.log(`Total Attempts: ${totalAttempts}`);
        console.log(`Total Blocks Found: ${totalBlocksFound}`);
        console.log(`Total Hashes: ${totalHashes.toLocaleString()}`);
        console.log(`Runtime: ${runtime.toFixed(2)}s`);
        console.log(`Combined Hashrate: ${avgHashrate.toLocaleString()} H/s`);
        console.log(`Success Rate: ${((totalBlocksFound / totalAttempts) * 100).toFixed(2)}%`);
        console.log(`\n💰 REWARD DESTINATION`);
        console.log(`   Wallet: ${this.walletAddress}`);
        console.log(`   Network: Bitcoin TESTNET`);
        console.log(`   Blocks Found: ${totalBlocksFound}`);
        if (totalBlocksFound > 0) {
            console.log(`   Estimated Rewards: ${(totalBlocksFound * 0.001).toFixed(8)} tBTC (testnet coins)`);
        }
        console.log(`${'='.repeat(80)}`);
        console.log(`\n✅ Multi-node mining session complete!`);
    }

    /**
     * Run sequential mining (one node at a time)
     */
    async startSequential(attemptsPerNode = 2) {
        console.log(`\n${'='.repeat(80)}`);
        console.log(`🔄 STARTING SEQUENTIAL MINING SESSION`);
        console.log(`${'='.repeat(80)}`);

        const results = [];

        for (let i = 0; i < this.miners.length; i++) {
            const miner = this.miners[i];
            console.log(`\n${'='.repeat(80)}`);
            console.log(`🖥️  Mining with node ${i + 1}/${this.numNodes}: ${miner.minerId}`);
            console.log(`${'='.repeat(80)}`);

            try {
                await miner.startMining(attemptsPerNode);
                results.push({
                    minerId: miner.minerId,
                    stats: miner.miningStats
                });
            } catch (error) {
                console.error(`❌ Error in ${miner.minerId}:`, error.message);
                results.push({
                    minerId: miner.minerId,
                    stats: miner.miningStats,
                    error: error.message
                });
            }
        }

        this.aggregateResults(results);
    }
}

// Main execution
async function main() {
    // Get wallet address from environment or use default testnet address
    const TESTNET_WALLET = process.env.WALLET || "tb1qfzhx87ckhn4tnkswhsth56h0gm5we4hdyscrle";
    const NUM_NODES = parseInt(process.env.NODES || '3');
    const ATTEMPTS_PER_NODE = parseInt(process.env.ATTEMPTS || '2');
    const MODE = process.env.MODE || 'parallel'; // 'parallel' or 'sequential'

    console.log(`\n${'='.repeat(80)}`);
    console.log(`⚛️  QUANTUM & CLASSICAL BITCOIN TESTNET MINING SYSTEM`);
    console.log(`${'='.repeat(80)}`);
    console.log(`Configuration:`);
    console.log(`  Wallet: ${TESTNET_WALLET}`);
    console.log(`  Nodes: ${NUM_NODES}`);
    console.log(`  Attempts per node: ${ATTEMPTS_PER_NODE}`);
    console.log(`  Mode: ${MODE.toUpperCase()}`);
    console.log(`${'='.repeat(80)}`);

    const manager = new MultiNodeManager(TESTNET_WALLET, NUM_NODES);
    manager.initializeNodes();

    if (MODE === 'sequential') {
        await manager.startSequential(ATTEMPTS_PER_NODE);
    } else {
        await manager.startAllNodes(ATTEMPTS_PER_NODE);
    }

    console.log(`\n${'='.repeat(80)}`);
    console.log(`🎓 EDUCATIONAL SUMMARY`);
    console.log(`${'='.repeat(80)}`);
    console.log(`\nWhat you just learned:`);
    console.log(`  ✅ How Bitcoin testnet mining works`);
    console.log(`  ✅ How multiple nodes compete for blocks`);
    console.log(`  ✅ How quantum vs classical mining would compare (simulated)`);
    console.log(`  ✅ How mining difficulty affects success rates`);
    console.log(`  ✅ How blocks are validated with proof-of-work`);
    console.log(`\nImportant notes:`);
    console.log(`  ⚠️  This uses Bitcoin TESTNET (test coins have no value)`);
    console.log(`  ⚠️  Quantum mining devices are simulated for education`);
    console.log(`  ⚠️  Real mining requires ASIC hardware and mining pools`);
    console.log(`  ⚠️  CPU mining has extremely low success probability`);
    console.log(`  ⚠️  To actually claim rewards, you need a full testnet node`);
    console.log(`\nNext steps to mine real testnet coins:`);
    console.log(`  1. Install Bitcoin Core in testnet mode`);
    console.log(`  2. Get testnet coins from a faucet: https://testnet-faucet.com`);
    console.log(`  3. Join a testnet mining pool`);
    console.log(`  4. Configure mining software (cgminer, bfgminer, etc.)`);
    console.log(`${'='.repeat(80)}\n`);
}

// Run if called directly
if (require.main === module) {
    main().catch(error => {
        console.error('\n❌ Fatal error:', error.message);
        process.exit(1);
    });
}

module.exports = MultiNodeManager;
