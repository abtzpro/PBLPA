# PBLPA - PowerBall Lottery Probability Analysis

- [Table of Contents](#table-of-contents)
  - [1. What's All The Fuss About?](#overview)
  - [2. Getting Your Hands Dirty - Installation](#installation-instructions)
  - [3. Time to Roll - How To Use](#instructions-for-use)
  - [4. Making It Your Own - Modification](#modification-instructions)
  - [5. Stuck in a Rut? - Troubleshooting](#troubleshooting-instructions)
  - [6. Let's Talk Science](#scientific-breakdowns)
  - [7. Deep Dive into Analysis and Research](#in-depth-analysis-and-research)
  - [8. Hats off - Sources Cited](#sources-cited)
  - [9. The Man Behind the Curtain - Developer Credits](#developer-credits)
  - [10. Putting It to Work - Use Cases](#use-cases)
  - [11. Getting Better Every Day - Improvements](#improvements)
  - [12. Wrapping Up](#conclusion)

## 1. What's All The Fuss About? <a name="overview"></a>

Welcome to PBLPA! It stands for PowerBall Lottery Probability Analysis - a bit of a mouthful, I know. It's a Python script I crafted to delve into the depths of PowerBall lottery data. The idea was to see if there's a way we could predict the outcomes of this lottery using machine learning or algorithms. Spoiler alert: we can't. More on that later.

## 2. Getting Your Hands Dirty - Installation <a name="installation-instructions"></a>

Ready to give this a spin? Great! Here's how:

1. Clone this repo to your machine.
2. Check you've got Python 3.7 or above. Use `python --version` in your command line if you're unsure.
3. Install the necessary Python packages with `pip install -r requirements.txt` in the project directory.

## 3. Time to Roll - How To Use <a name="instructions-for-use"></a>

Let's get it up and running:

1. Navigate to the project directory in your command line.
2. Use the magic phrase `python PBLPA.py`.

## 4. Making It Your Own - Modification <a name="modification-instructions"></a>

Fancy tweaking this for your own purposes? No problem. If you want to analyze a different lottery, change the `url` in the `main` function and you may also need to adjust the `parse_html` function to suit the webpage structure.

## 5. Stuck in a Rut? - Troubleshooting <a name="troubleshooting-instructions"></a>

If you're running into trouble:

1. Double-check you've installed and updated all required Python packages.
2. Make sure you have internet access and permission to spawn browser instances.
3. Check your Chrome WebDriver is installed and compatible with your version of Chrome.
4. If you've been playing around with the script, look for any potential errors in your changes.

## 6. Let's Talk Science <a name="scientific-breakdowns"></a>

Here's where we delve into the nitty-gritty. PBLPA is based on probability. It fetches all the PowerBall draws, works out the frequency of each number, and calculates each one's probability by dividing by the total number of draws. You might think, "Well, if a number comes up more often, it's more likely to appear in future, right?" Not quite, and we'll get into why in the following sections.

## 7. Deep Dive into Analysis and Research <a name="in-depth-analysis-and-research"></a>

As a data scientist, I'm all about spotting trends and patterns. But here's the kicker - in a pure chance game like the lottery, there are no patterns. Each draw is completely independent and random. This poses a problem for machine learning algorithms that thrive on patterns.

You could only predict a lottery draw outcome if you knew the exact state (the "seed") of the random number generator when the draw is made. But that info is kept under wraps to ensure fair play. 

## 8. Hats off - Sources Cited <a name="sources-cited"></a>

Big shoutout to:

- PowerBall Official Website: https://www.powerball.com/
- Python Official Documentation: https://docs.python.org/3/
- Selenium Python Bindings Documentation: https://selenium-python.readthedocs.io/
- BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## 9. The Man Behind the Curtain - Developer Credits <a name="developer-credits"></a>

This is the work of Adam Rivers - a data scientist with a healthy obsession for all things data and machine learning.

https://abtzpro.github.io

## 10. Putting It to Work - Use Cases <a name="use-cases"></a>

Despite its inability to predict lottery numbers, PBLPA can still shine a light on some interesting stuff:

- Checking out the frequency of drawn numbers.
- Observing trends over time, like frequencies evening out.
- Validating the randomness of lottery draws.

## 11. Getting Better Every Day - Improvements <a name="improvements"></a>

There's always room for improvement:

- Speeding things up by optimizing the web scraping process.
- Adding error handling for website structure changes.
- Including options to analyze different time periods.

## 12. Wrapping Up <a name="conclusion"></a>

So there you have it - PBLPA in all its glory. It won't make you a millionaire, but it offers a neat way to dive into lottery data, explore probability, and test assumptions. Remember, lottery games like PowerBall are a game of chance, and that's all part of the fun. Happy exploring!
