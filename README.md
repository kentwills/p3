<body>
<h2>CS 723 Project 3: Multilingual Lexical Semantics</h2>

<h3>Table of Contents</h3>
<ul>
<li><a href="#intro">Introduction</a>
<li><a href="#wsd">Multilingual WSD (100%)</a>
</ul>

<h3><a name="intro">Introduction</a></h3>

In contrast to P1, where most of the info was here, this doc is now
just a schematic and the main details are in the relevant .py files.

<p>The code for this project consists of several Python files, some of
which you will need to read and understand in order to complete the
assignment, and some of which you can ignore. You can download all the
code and supporting files (including this description) as
a <a href="p3.tar.gz">tar archive</a> (this one is kind of big due to
the large amount of included data).

<table border="0" cellpadding="10">
<tr><td colspan="2"><b>Files you'll edit:</b></td></tr>
  
  <tr><td><code>wsd.py</code></td>
  <td>Where you'll implement multilingual word sense disambiguation </td></tr>
  
<tr><td colspan="2"><b>Files you might want to look at:</b></td></tr>
  
  <tr><td><code>wsddata.py</code></td>
  <td>I/O functions for wsd.</td></tr>

  <tr><td><code>util.py</code></td>
  <td>A handful of useful utility functions: these will undoubtedly be helpful to you, so take a look!</td></tr>
</table>
<p>

<p><strong>Evaluation:</strong> Your code will be autograded for
technical correctness. Please <em>do not</em> change the names of any
provided functions or classes within the code, or you will wreak havoc
on the autograder.  However, the correctness of your implementation --
not the autograder's output -- will be the final judge of your score.
If necessary, we will review and grade assignments individually to
ensure that you receive due credit for your work.

<p><strong>Academic Dishonesty:</strong> We will be checking your code
against other submissions in the class for logical redundancy. If you
copy someone else's code and submit it with minor changes, we will
know. These cheat detectors are quite hard to fool, so please don't
try. We trust you all to submit your own work only; <em>please</em>
don't let us down. If you do, we will pursue the strongest
consequences available to us.

<p><strong>Getting Help:</strong> You are not alone!  If you find
yourself stuck on something, contact the course staff for help.
Office hours, class time, and Piazza are there for your support;
please use them.  If you can't make our office hours, let us know and
we will schedule more.  We want these projects to be rewarding and
instructional, not frustrating and demoralizing.  But, we don't know
when or how to help unless you ask.  One more piece of advice: if you
don't know what a variable is, print it out.


<h3><a name="wsd"></a>Multilingual WSD <i>(100%)</i></h3>

Your task is to do translation-sense disambiguation by
implementing features that will be useful for this task.  If you look
at "Science.ambig" you'll see some ambiguous french words that you
need to pick the correct translation of given context.  Note that some
of these are boring morphological distinctions, while some are
interesting WSD distinctions (like alteration being either adjustment
or damage, depending on context).</p>

The basic setup is that you will be give a French word in context (the
entire document context) from this list of French words and you need
to pick the correct translation.  To do so, you can define features of
the French context that you believe will help disambiguate (for
instance, the word "money" in the context of "bank" might help
disambiguate what type of bank you're talking about).  You can also
define features of the English translation (perhaps its suffix, so you
know what part of speech you're translating into).  Finally, you can
define features of the pair of the French word and English word.  For
instance, string edit distance might be useful to pick up cognates
(eg., ajustement/adjusting or homologue/homologous).<p/>

To get you started, I have some very stupid features implemented in
simpleEFeatures, simpleFFeatures and simplePairFeatures.  Before
implementing anything else, you should be able to get about 70%
accuracy at this task (don't be impressed: you get this more or less
just by choosing the most frequent sense, which is actually a VERY
HARD baseline to beat!):<p/>

<pre>
% python wsd.py
reading data from  Science.tr
reading data from  Science.de
collecting translation table
generating classification data
executing:  /home/hal/bin/vw -k -c --holdout_off --passes 10 -q st --power_t 0.5 --csoaa_ldf m -d wsd_vw.tr -f wsd_vw.model --quiet
executing:  /home/hal/bin/vw -t -q st -d wsd_vw.tr -i wsd_vw.model -r wsd_vw.tr.rawpredictions --quiet
executing:  /home/hal/bin/vw -t -q st -d wsd_vw.te -i wsd_vw.model -r wsd_vw.te.rawpredictions --quiet
training accuracy = 0.696218640165
testing  accuracy = 0.695172634271
</pre>

In order for this to work, you need to be sure
that <a href="https://github.com/JohnLangford/vowpal_wabbit/wiki/Download">VW</a>
is installed on your system, and that it's pointed to correctly at the
top of the file wsddata.py.</p>

Once you implement the suggested features I gave you, you should do
markedly better:<p/>

<pre>
% python wsd.py
...
training accuracy = 0.999010220983
testing  accuracy = 0.715952685422
</pre>

70% of your grade on this part is based on being able to replicate
that.  The rest, as you probably expect by now, is to beat this
baseline by coming up with, and implementing, useful features.  For
every half a percent that you get over my baseline, you'll get two
percent toward the remaining 30%.  In addition, the top team will get
5%, the second 4%, third 3%, fourth 2% and fifth 1%.  If it turns out
no one gets full credit, I'll adjust these thresholds in your favor
(but never against your favor).</p>

As usual, you should develop on the dev data and then hand in your
results on the test data.  Implement your fancy features in the
complex functions, and then run on Science.te (by changing the main
definition) and upload the output stored in wsd_output.  You can view
your progress on the <a href="leaderboard.html">leaderboard</a>.

<b>Extra credit:</b> If you're feeling adventurous, you can also work
on movie subtitles data instead of scientific articles (but don't get
mad at me that they swear a lot in that data).  You should download
the <a href="subs.tgz">Subtitles</a> data separately and you can hand
in (optionally) your output on subs for extra credit.  This is purely
optional.  If you beat my baseline by at least 1%, you get 5% extra
credit.  First place team gets 5% more, second 3% and third 2%.  Note
that this data is <i>much</i> larger, and the documents are much
longer (they are whole movies!) so you might run in to scaling
problems.


</body>
</html>
