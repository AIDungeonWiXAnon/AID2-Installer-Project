# Datasets and information for training and finetuning AI
----------------------------
This page needs a lot of work, please feel free to edit it and submit changes.

No one has quite worked out a great method of retraining the AI, but many anons are trying different things and progress is being made. I have my own approach I'm working on but can't promise anything anytime soon. But I'll take any datasets you want to link me.

## GNU/UNIX tools
----------
Windows users I'm sorry but your software sucks for things that involve manipulating text files. Fortunately you guys have the windows subsystem for linux which allows you to use all the basic unix tools within windows. I'm just throwing some basic info here for noobs that have no idea what to do. Go to [/g/fglt](https://boards.4channel.org/g/catalog#s=fglt) for help with GNU/linux tools and questions.

### `wget`
---------------------------
`wget` is THE greatest tool for scraping websites. Read the man page even though it is long, there are so many useful options (`man wget` noobs.)
You can scrape an entire website with something like this command: `wget -m website`

### `elinks`
----------------
Once you have a bunch of scraped html files, you can convert them to txt files using elinks -dump option. Be sure to read the man page. You will probably want -dump-width 999 or as high as it will go, to disable it's default word wrapping.

### `sed`
------------
`sed` is useful for filtering unwanted words or patterns out of files using it's substitution command.  You need to use `info sed` to read it's documentation.

### misc
------------
`pdftotext` from poppler utils - does what it says on the tin
`iconv` to convert weird document encodings to ascii. Especially useful with pdf data that often has converted common character combinations to weird unicode ligatures.


# Datasets
------------------------
The mormon used a dataset of CYOA texts that can still be found in the data folder of this repo. There are references to other datasets as well. 

For example a script used to scrape the /r/writingprompts subreddit, a subreddit where people post short stories. We can get these files pre-scraped by facebook: 
https://github.com/pytorch/fairseq/tree/master/examples/stories

There are also references in the code to mechanical turk, a website used to pay thirdworlders to enter data for you for pennies.

Large collection of CYOA text: https://editthis.info/create_your_own_story/ Including an adult category: https://editthis.info/create_your_own_story/Category:Adult_Stories All in the format of a mediawiki. See https://wiki.installgentoo.com/wiki/Wiki_Backups for info on scraping mediawikis. Also see the section on wget. 

Project Gutenberg has over 60,000 public domain books that have been manually transcribed into text files. Most of these books are quite old. Virtually all pre-1920s.

Some anon a few days ago claimed to have >18,000 sci fi and fantasy novels in an epub format. I can no longer find his post, would love to have that.

Anon says chyoa.com has many CYOA stories including lewd ones

Every *Welcome to Night Vale* Transcript. (Interesting because *Welcome to Night Vale*'s surreal and absurd setting fits with the randomness of the AI's output): https://gofile.io/?c=AOTOEs

Kono Sekai ga Game da to Ore dake ga Shitteiru (This World Is a Game, but Only I Know It: volume 1 & 2)
https://gofile.io/?c=M1Tzye

Goblin Slayer (volume 1 - 8)
https://gofile.io/?c=BwP9ru

-Bionicle txt (books up to Mahri Nui, handful of lego web series + few lewd fanfics)
https://gofile.io/?c=dcIruE
-Witcher books
https://gofile.io/?c=Qp8dKQ
