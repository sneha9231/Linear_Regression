{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNWp/Rsc22KvuUmdC0nPoWA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sneha9231/Linear_Regression/blob/main/Linear_Regression.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 147
        },
        "id": "7tcUmY1-Tqpo",
        "outputId": "126e42e3-fdf6-44f8-b0ce-8daffd37252e"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Linear regression is a statistical method that is used to predict a continuous dependent variable(target variable) based on one or more\\nindependent variables(predictor variables). This technique assumes a linear relationship between the dependent and independent variables,\\nwhich implies that the dependent variable changes proportionally with changes in the independent variables. In other words, linear regression is\\nused to determine the extent to which one or more variables can predict the value of the dependent variable.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "'''Linear regression is a statistical method that is used to predict a continuous dependent variable(target variable) based on one or more\n",
        "independent variables(predictor variables). This technique assumes a linear relationship between the dependent and independent variables,\n",
        "which implies that the dependent variable changes proportionally with changes in the independent variables. In other words, linear regression is\n",
        "used to determine the extent to which one or more variables can predict the value of the dependent variable.'''\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "DBhcOaT4U3bq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Read the dataset using read_csv() function\n",
        "df=pd.read_csv('advertising-1.csv')\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "zQaKBzbuU8DW",
        "outputId": "7245a274-0cd1-4604-8bb4-dc52c7b2228e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      TV  Radio  Newspaper  Sales\n",
              "0  230.1   37.8       69.2   22.1\n",
              "1   44.5   39.3       45.1   10.4\n",
              "2   17.2   45.9       69.3   12.0\n",
              "3  151.5   41.3       58.5   16.5\n",
              "4  180.8   10.8       58.4   17.9"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-905fb415-7715-459d-a67a-29dcec0c783c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>TV</th>\n",
              "      <th>Radio</th>\n",
              "      <th>Newspaper</th>\n",
              "      <th>Sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>230.1</td>\n",
              "      <td>37.8</td>\n",
              "      <td>69.2</td>\n",
              "      <td>22.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>44.5</td>\n",
              "      <td>39.3</td>\n",
              "      <td>45.1</td>\n",
              "      <td>10.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>17.2</td>\n",
              "      <td>45.9</td>\n",
              "      <td>69.3</td>\n",
              "      <td>12.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>151.5</td>\n",
              "      <td>41.3</td>\n",
              "      <td>58.5</td>\n",
              "      <td>16.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>180.8</td>\n",
              "      <td>10.8</td>\n",
              "      <td>58.4</td>\n",
              "      <td>17.9</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-905fb415-7715-459d-a67a-29dcec0c783c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-905fb415-7715-459d-a67a-29dcec0c783c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-905fb415-7715-459d-a67a-29dcec0c783c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-028c42cf-f4ee-4777-b5e7-c05f3a382116\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-028c42cf-f4ee-4777-b5e7-c05f3a382116')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-028c42cf-f4ee-4777-b5e7-c05f3a382116 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 200,\n  \"fields\": [\n    {\n      \"column\": \"TV\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 85.85423631490808,\n        \"min\": 0.7,\n        \"max\": 296.4,\n        \"samples\": [\n          287.6,\n          286.0,\n          78.2\n        ],\n        \"num_unique_values\": 190,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Radio\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14.846809176168724,\n        \"min\": 0.0,\n        \"max\": 49.6,\n        \"samples\": [\n          8.2,\n          36.9,\n          44.5\n        ],\n        \"num_unique_values\": 167,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Newspaper\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 21.778620838522826,\n        \"min\": 0.3,\n        \"max\": 114.0,\n        \"samples\": [\n          22.3,\n          5.7,\n          17.0\n        ],\n        \"num_unique_values\": 172,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5.283892252561876,\n        \"min\": 1.6,\n        \"max\": 27.0,\n        \"samples\": [\n          19.8,\n          22.6,\n          17.9\n        ],\n        \"num_unique_values\": 121,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WUz7Pn2MU-Rq",
        "outputId": "3a124476-e501-44d2-e6b4-8c3183940ed1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(200, 4)"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VBeyuXqhVECq",
        "outputId": "76fcfa8d-eb67-41de-8129-d04a813d038a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 200 entries, 0 to 199\n",
            "Data columns (total 4 columns):\n",
            " #   Column     Non-Null Count  Dtype  \n",
            "---  ------     --------------  -----  \n",
            " 0   TV         200 non-null    float64\n",
            " 1   Radio      200 non-null    float64\n",
            " 2   Newspaper  200 non-null    float64\n",
            " 3   Sales      200 non-null    float64\n",
            "dtypes: float64(4)\n",
            "memory usage: 6.4 KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Checking for NULL value in dataset\n",
        "df.isnull()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "aTmtLLYcVHbL",
        "outputId": "b55b30af-3ca8-48a2-ac5e-3ef3388e132f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        TV  Radio  Newspaper  Sales\n",
              "0    False  False      False  False\n",
              "1    False  False      False  False\n",
              "2    False  False      False  False\n",
              "3    False  False      False  False\n",
              "4    False  False      False  False\n",
              "..     ...    ...        ...    ...\n",
              "195  False  False      False  False\n",
              "196  False  False      False  False\n",
              "197  False  False      False  False\n",
              "198  False  False      False  False\n",
              "199  False  False      False  False\n",
              "\n",
              "[200 rows x 4 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-60f6fff5-dd01-48de-a10c-a2bab21209cf\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>TV</th>\n",
              "      <th>Radio</th>\n",
              "      <th>Newspaper</th>\n",
              "      <th>Sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>195</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>196</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>197</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>198</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>199</th>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>200 rows × 4 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-60f6fff5-dd01-48de-a10c-a2bab21209cf')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-60f6fff5-dd01-48de-a10c-a2bab21209cf button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-60f6fff5-dd01-48de-a10c-a2bab21209cf');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-b7cd8698-c86c-401e-b62b-49319cca360e\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-b7cd8698-c86c-401e-b62b-49319cca360e')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-b7cd8698-c86c-401e-b62b-49319cca360e button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 200,\n  \"fields\": [\n    {\n      \"column\": \"TV\",\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"samples\": [\n          false\n        ],\n        \"num_unique_values\": 1,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Radio\",\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"samples\": [\n          false\n        ],\n        \"num_unique_values\": 1,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Newspaper\",\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"samples\": [\n          false\n        ],\n        \"num_unique_values\": 1,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Sales\",\n      \"properties\": {\n        \"dtype\": \"boolean\",\n        \"samples\": [\n          false\n        ],\n        \"num_unique_values\": 1,\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.heatmap(df.corr(),annot=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 453
        },
        "id": "7wNJGR90VLJh",
        "outputId": "3136f60a-e794-48cd-e5cc-0de1e53d04d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 7
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=df[['TV']]\n",
        "y=df['Sales']"
      ],
      "metadata": {
        "id": "ULYz68NFVO3q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=2) #splitting datset into testing and trained set"
      ],
      "metadata": {
        "id": "-BZHLgSWVRe5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression"
      ],
      "metadata": {
        "id": "7WImWGZ8VWoZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model=LinearRegression() #creating and training linear regression model\n",
        "model.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "BtX9BUC1VbV5",
        "outputId": "29949ad2-4868-4d0d-9fbb-f0909c6dea0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred=model.predict(x_test)"
      ],
      "metadata": {
        "id": "2A1rWJ4uVeCx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(x_train,y_train,color='g')\n",
        "plt.plot(x_test,y_pred,color='m')"
      ],
      "metadata": {
        "id": "1x1mUFmfVgUT",
        "outputId": "ab4d1a7b-8951-493c-c5c5-47222187de44",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7efd99d6f610>]"
            ]
          },
          "metadata": {},
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "PIfppMQlV0U_"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
