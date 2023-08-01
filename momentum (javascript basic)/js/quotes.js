const quotes = [
    {
        quotes: "There are two kinds of people in this world:\
        those who want to get things done and those who don't want to make mistakes",
        author: "John Maxwell",
    },
    {
        quotes: "Without continuous personal development, you are now all that you will ever become\
         and hell starts when the person you are meets the person you could have been.",
        author: "Eli cohen",
    },
    {
        quotes: "I find that the harder I work, the more luck I seem to have.",
        author: "Thomas Jefferson",
    },
    {
        quotes: "Move out of your comfort zone. You can only grow if you are willing to\
         feel awkward and uncomfortable when you try something new.",
        author: "Brian Tracy "
    },
    {
        quotes: "Don't let the fear of losing be greater than the excitement of winning.",
        author: "Robert Kiyosaki"
    },
    {
        quotes: "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.",
        author: "Dale Carnegie"
    },
    {
        quotes: "Action is the foundational key to all success.",
        author: "Pablo Picasso"
    },
]

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");
const todayQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todayQuote.quotes;
author.innerText = todayQuote.author;