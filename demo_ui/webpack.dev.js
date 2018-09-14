const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')

module.exports = {
    entry: './app/index.js',
    output: {
        path: path.resolve('build'),
        filename: 'bundle.js'
    },
    module: {
        rules: [
            { 
                test: /\.js$/, 
                exclude: /node_modules/,
                use: [
                    "babel-loader",
                    {
                        loader: "eslint-loader",
                        options: {
                            fix: true,
                        }
                    }
                ]
            },
            {
                test: /\.css$/,
                use: [{ loader: 'style-loader' }, { loader: 'css-loader' }],
            },
            {
                test: /\.scss$/,
                loader: "style-loader!css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]!sass-loader",
                include: /(app)/
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./app/index.html",
            filename: "index.html",
            inject: "body"
        }),

        new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/)
    ],
    devServer: {
        port: 9000,
        proxy: {
            //"/api": "http://localhost:8000"
        }
    }
}