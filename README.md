<h2 align="center">
  <img src="https://cdn.discordapp.com/attachments/775096810963468288/893470193911734272/1.png" height='100px' width='100px'>
</h2>

<h1 align="center">[>]GraphBot</h1>
<h4 align="center">A simple Graphing Discord bot.</h4>

<h1 align="center">
  <a href="https://top.gg/bot/851532461061308438">
      <img src="https://top.gg/api/widget/status/851532461061308438.svg" alt="[>]GraphingBot" />
  </a>
  <a href="https://top.gg/bot/851532461061308438">
      <img src="https://top.gg/api/widget/servers/851532461061308438.svg" alt="[>]GraphingBot" />
  </a>
  <a href="https://top.gg/bot/851532461061308438">
      <img src="https://top.gg/api/widget/upvotes/851532461061308438.svg" alt="[>]GraphingBot" />
  </a><br>
  <img src="https://img.shields.io/badge/discord.py-2.0-blue?style=flat" />
  <img src="https://img.shields.io/badge/Python-3.9-green?style=flat&logo=python" />
</h1>

<h2><img src="https://cdn.discordapp.com/emojis/766498653753049109.png?v=1" height="20px"> • Info</h2>

<p>This is a Basic Graphing Bot and is a showcase of Denzven-Graphing-Api to plot flat,polar and 3-dimensional graphs using the input formula</p>


<html>
<style type="text/css">
  @import url('https://cdn.jsdelivr.net/gh/denzven/Denzven-Graphing-Api-Bot@master/topgg_css.css');

</style>

<section id="main_content">

<h1 id="denzven-graphing-api-bot">Denzven-Graphing-Api-Bot</h1>
<h3 id="welcome-this-is-an-example-bot-made-for-showcasing-the-abilties-of-denzven-graphing-api">Welcome! this is an Example Bot made for showcasing the abilties of <a href="https://denzven.pythonanywhere.com/">Denzven-Graphing-Api</a></h3>

<h3 id="1-about-the-api">1. About the Api:</h3>

<p>Denzven-Graphing-Api is my first flask project that plots graphs of formulas/Equations using python. i have also made and <a href="https://pypi.org/project/Denzven-Graphing-Api-Wrapper">Api-Wrapper</a> (mostly for practice) to make life easy and to use this Api.</p>

<hr>

<h3 id="2-how-to-use-the-api">2. How to Use the Api?</h3>

<p>Using the Api is as simple as sending a request to the <a href="https://denzven.pythonanywhere.com/">website</a> with some params such as the fourmula ,grid ,plot_stylee ,x_coord ,y_coord (and more params coming..) and the Api will return an image of the plotted Graph.</p>

<h4 id="example-of-a-requested-url">Example of a requested url:</h4>

<blockquote>
  <p>http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot?formula=x%2By&amp;x%2By&amp;grid=1&amp;plot_style=3&amp;x_coord=20&amp;y_coord=20</p>
</blockquote>

<p><img src="https://cdn.discordapp.com/attachments/814689514463297538/859139715948871690/unknown.png" alt="Graph Example in Discord"></p>

<p>Note:</p>
<ul>
  <li>Base url:
    <ul>
      <li>http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot</li>
    </ul>
  </li>
  <li>the formula:
    <ul>
      <li>?formula=x%2By&amp;x%2By
        <blockquote>
          <p>Note that this url is “urlencoded” using urllib.</p>
        </blockquote>
      </li>
      <li>what can the formula contain?
        <ul>
          <li>trignometric functions:
            <blockquote>
              <p>sin() cos() tan()</p>
            </blockquote>
          </li>
          <li>powers
            <blockquote>
              <p>x**2 = x²</p>
            </blockquote>
          </li>
          <li>Basic BODMAS
            <blockquote>
              <p>()=Brackets, <br>
  /=Divide, <br>
  *=Mutiply,<br>
  +=Add,<br>
  -=Subtract</p>
            </blockquote>
          </li>
          <li>Misc:
            <blockquote>
              <p>pi=value of the const pi,<br>
  sqrt()=square root of the value,<br>
  %=modulos gives the remaider of the divsion</p>
            </blockquote>
            <ul>
              <li>eg: 2%6=0 and 2%(10)=0</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>the params:
    <ul>
      <li>&amp;grid=1
        <blockquote>
          <p>grid refers to the presence of smaller grid lines, 1 is true and 0 is false</p>
        </blockquote>
      </li>
      <li>&amp;plot_style=3
        <blockquote>
          <p>these are a list of the default plot_styles it can range from 0-25</p>
        </blockquote>
      </li>
      <li>&amp;x_coord=20
        <blockquote>
          <p>the value ot the x coordinate (horizontal)</p>
        </blockquote>
      </li>
      <li>&amp;y_coord=20
        <blockquote>
          <p>the value ot the y coordinate (vertical)</p>
        </blockquote>
      </li>
    </ul>
  </li>
</ul>

<hr>

<h3 id="3-limitations-of-the-api">3. Limitations of the Api</h3>

<p>The api has several limitations in its use now, and is slowly getting patched/fixed.</p>

<p>Some Known ones:</p>
<ul>
  <li>limitations in the formula usage: the formula must equate to zero.<br>
like “x+y” as input will mean the graph of “x+y=0” and it must contain bot x and y in the equation.</li>
</ul>

<p>I dont know of any other feel free to add them in!</p>

<hr>
<h3 id="4-contributing-to-the-api-if-you-want-to-add-changesneaten-up-the-code">4. Contributing to the Api (if you want to add changes/neaten up the code)</h3>

<ul>
  <li><a href="https://github.com/denzven/Denzven-Graphing-Api-Bot/fork">Fork the repository</a></li>
  <li>Clone your fork: <code class="language-plaintext highlighter-rouge">git clone https://github.com/denzven/Denzven-Graphing-Api-Bot.git</code></li>
  <li>Create your feature branch: <code class="language-plaintext highlighter-rouge">git checkout -b my-new-feature</code></li>
  <li>Commit your changes: <code class="language-plaintext highlighter-rouge">git commit -am 'Add some feature'</code></li>
  <li>Push to the branch: <code class="language-plaintext highlighter-rouge">git push origin my-new-feature</code></li>
  <li>Submit a pull request</li>
</ul>

<h3 id="5-known-bugs-and-issue-reporting">5. Known Bugs and Issue reporting</h3>

<ul>
  <li>there was a bug by putting exit() or quit() in the formula that would turn off the api.. i have tried my best to patch it</li>
</ul>

<p>I dont know of any other feel free to add them in!</p>

<h3 id="6-about-me">6. About Me</h3>

<p>I am a 17 year old wierdo that hops on with tons of hobbies and gets bored easily. Tried out a bunch of stuff like blender3D, voxel art, making discord bots and telegram bots, basic python programs, right now i am making an Graphing API and its wrapper.
you can find more info about me <a href="https://denzven.pythonanywhere.com">here</a></p>

<p>Thank you! Hope You can tribute much needed support and enjoy using the api as much i did making it 😁</p>

</section>

<iframe src="https://denzven.pythonanywhere.com" width="100%" height="1250px"></iframe>
</html>
