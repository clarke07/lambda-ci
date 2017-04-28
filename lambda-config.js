module.exports = {

    region: 'us-west-2',
    handler: 'index.handler',
    role: 'arn:aws:iam::037346530273:role/APIGatewayLambdaExecRole',
    functionName: 'clarkeTestLambdaCI',
    timeout: 10,
    memorySize: 128,
    runtime: 'nodejs'
}