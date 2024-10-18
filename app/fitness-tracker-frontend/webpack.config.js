const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js', // The entry point of your app
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/, // Regex to look for .js and .jsx files
        exclude: /node_modules/, // Ignore node_modules folder
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/, // Regex for CSS files
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'], // File extensions for imports
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // Template HTML file
    }),
  ],
  devServer: {
    static: './dist',
    hot: true, // Enable Hot Module Replacement for faster dev
    open: true, // Automatically open the app in the browser
  },
  mode: 'development', // Set to 'production' when you are ready to deploy
};
