const path = require('path');

const publicDir = path.join(__dirname, '/public');
module.exports = {
    entry: [
        './src/index.jsx',
    ],
    output: {
        path: publicDir,
        publicPath: '/',
        filename: 'bundle.js',
    },
    module: {
        rules:[{
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
                presets: ['react', 'es2015'],
            },
        }]
    },
    resolve: {
        extensions: ['.js', '.jsx'],
    },
    devServer: {
        historyApiFallback: true,
        contentBase: publicDir,
        port: 3000,
    },
};
