# Reddit Community Detection Using Graphs

This project aims to detect communities on Reddit using graph traversal and search techniques. We utilize the "Reddit Hyperlink Network" dataset, which consists of a network of subreddits and their relationships based on shared links. The dataset includes information about subreddits, the number of subscribers, and interactions between subreddits in the form of shared links. For this project, we will only use the first 5,000 nodes.

Try this project in [Google Colab](https://colab.research.google.com/drive/1YD2y_J6_5IvdlrzEXOD1yQHtx-mlFesO?usp=sharing)

![Image of first 20 nodes](https://github.com/oliverTuesta/reddit-communities-reddit/blob/main/images/first_20_nodes.png)

## Tools

-   Python
-   Jupyter Notebook
-   NetworkX
-   Pandas
-   Matplotlib

## Getting Started

1. Clone this repository to your local machine.
2. Ensure you have Python and Jupyter Notebook installed.
3. Install the required libraries: NetworkX, Pandas, and Matplotlib.
4. Open the `app.ipynb` file in Jupyter Notebook and run the cells to see the results.

## Project Structure

-   `app.ipynb`: Main Jupyter Notebook file containing the code for community detection.
-   `soc-redditHyperlinks-title-5000.tsv`: Dataset containing the first 5,000 nodes from the <a href="http://snap.stanford.edu/data/soc-RedditHyperlinks.html">Reddit Hyperlink Network</a>.

## Collaborators

-   Oliver Tuesta
-   Arnol Caceres
-   Yoimer Davila

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
