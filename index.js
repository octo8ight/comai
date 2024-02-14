const web3 = require("@solana/web3.js");
// const nacl = require("tweetnacl");

// // Airdrop SOL for paying transactions
// let payer = web3.Keypair.generate();
// let connection = new web3.Connection(web3.clusterApiUrl("devnet"), "confirmed");

// let airdropSignature = connection.requestAirdrop(
//   payer.publicKey,
//   web3.LAMPORTS_PER_SOL,
// );

// connection.confirmTransaction({ signature: airdropSignature });

// let toAccount = web3.Keypair.generate();

// // Create Simple Transaction
// let transaction = new web3.Transaction();

// // Add an instruction to execute
// transaction.add(
//   web3.SystemProgram.transfer({
//     fromPubkey: payer.publicKey,
//     toPubkey: toAccount.publicKey,
//     lamports: 1000,
//   }),
// );

// // Send and confirm transaction
// // Note: feePayer is by default the first signer, or payer, if the parameter is not set
// web3.sendAndConfirmTransaction(connection, transaction, [payer]);

// // Alternatively, manually construct the transaction
// let recentBlockhash = connection.getRecentBlockhash();
// let manualTransaction = new web3.Transaction({
//   recentBlockhash: recentBlockhash.blockhash,
//   feePayer: payer.publicKey,
// });
// manualTransaction.add(
//   web3.SystemProgram.transfer({
//     fromPubkey: payer.publicKey,
//     toPubkey: toAccount.publicKey,
//     lamports: 1000,
//   }),
// );

// let transactionBuffer = manualTransaction.serializeMessage();
// let signature = nacl.sign.detached(transactionBuffer, payer.secretKey);

// manualTransaction.addSignature(payer.publicKey, signature);

// let isVerifiedSignature = manualTransaction.verifySignatures();
// console.log(`The signatures were verified: ${isVerifiedSignature}`);

// // The signatures were verified: true

// let rawTransaction = manualTransaction.serialize();

// web3.sendAndConfirmRawTransaction(connection, rawTransaction);