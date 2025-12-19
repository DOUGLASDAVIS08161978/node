#!/usr/bin/env node

/**
 * Quick test script for Bitcoin testnet mining
 */

const TestnetMiner = require('./testnet_miner');

async function quickTest() {
    console.log('🧪 Running quick testnet mining test...\n');

    // Use testnet address
    const TESTNET_WALLET = "tb1qfzhx87ckhn4tnkswhsth56h0gm5we4hdyscrle";

    const miner = new TestnetMiner(TESTNET_WALLET, 'test-node');

    try {
        // Run just 1 mining attempt for testing
        await miner.startMining(1);
        console.log('\n✅ Test completed successfully!');
    } catch (error) {
        console.error('\n❌ Test failed:', error.message);
        process.exit(1);
    }
}

quickTest();
