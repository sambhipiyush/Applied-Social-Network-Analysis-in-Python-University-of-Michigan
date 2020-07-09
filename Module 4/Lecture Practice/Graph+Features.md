
# Creating a feature matrix from a networkx graph

In this notebook we will look at a few ways to quickly create a feature matrix from a networkx graph.


```python
import networkx as nx
import pandas as pd

G = nx.read_gpickle('major_us_cities')
```

## Node based features


```python
G.nodes(data=True)
```




    [('El Paso, TX', {'location': (-106, 31), 'population': 674433}),
     ('Long Beach, CA', {'location': (-118, 33), 'population': 469428}),
     ('Dallas, TX', {'location': (-96, 32), 'population': 1257676}),
     ('Oakland, CA', {'location': (-122, 37), 'population': 406253}),
     ('Albuquerque, NM', {'location': (-106, 35), 'population': 556495}),
     ('Baltimore, MD', {'location': (-76, 39), 'population': 622104}),
     ('Raleigh, NC', {'location': (-78, 35), 'population': 431746}),
     ('Mesa, AZ', {'location': (-111, 33), 'population': 457587}),
     ('Arlington, TX', {'location': (-97, 32), 'population': 379577}),
     ('Sacramento, CA', {'location': (-121, 38), 'population': 479686}),
     ('Wichita, KS', {'location': (-97, 37), 'population': 386552}),
     ('Tucson, AZ', {'location': (-110, 32), 'population': 526116}),
     ('Cleveland, OH', {'location': (-81, 41), 'population': 390113}),
     ('Louisville/Jefferson County, KY',
      {'location': (-85, 38), 'population': 609893}),
     ('San Jose, CA', {'location': (-121, 37), 'population': 998537}),
     ('Oklahoma City, OK', {'location': (-97, 35), 'population': 610613}),
     ('Atlanta, GA', {'location': (-84, 33), 'population': 447841}),
     ('New Orleans, LA', {'location': (-90, 29), 'population': 378715}),
     ('Miami, FL', {'location': (-80, 25), 'population': 417650}),
     ('Fresno, CA', {'location': (-119, 36), 'population': 509924}),
     ('Philadelphia, PA', {'location': (-75, 39), 'population': 1553165}),
     ('Houston, TX', {'location': (-95, 29), 'population': 2195914}),
     ('Boston, MA', {'location': (-71, 42), 'population': 645966}),
     ('Kansas City, MO', {'location': (-94, 39), 'population': 467007}),
     ('San Diego, CA', {'location': (-117, 32), 'population': 1355896}),
     ('Chicago, IL', {'location': (-87, 41), 'population': 2718782}),
     ('Charlotte, NC', {'location': (-80, 35), 'population': 792862}),
     ('Washington D.C.', {'location': (-77, 38), 'population': 646449}),
     ('San Antonio, TX', {'location': (-98, 29), 'population': 1409019}),
     ('Phoenix, AZ', {'location': (-112, 33), 'population': 1513367}),
     ('San Francisco, CA', {'location': (-122, 37), 'population': 837442}),
     ('Memphis, TN', {'location': (-90, 35), 'population': 653450}),
     ('Los Angeles, CA', {'location': (-118, 34), 'population': 3884307}),
     ('New York, NY', {'location': (-74, 40), 'population': 8405837}),
     ('Denver, CO', {'location': (-104, 39), 'population': 649495}),
     ('Omaha, NE', {'location': (-95, 41), 'population': 434353}),
     ('Seattle, WA', {'location': (-122, 47), 'population': 652405}),
     ('Portland, OR', {'location': (-122, 45), 'population': 609456}),
     ('Tulsa, OK', {'location': (-95, 36), 'population': 398121}),
     ('Austin, TX', {'location': (-97, 30), 'population': 885400}),
     ('Minneapolis, MN', {'location': (-93, 44), 'population': 400070}),
     ('Colorado Springs, CO', {'location': (-104, 38), 'population': 439886}),
     ('Fort Worth, TX', {'location': (-97, 32), 'population': 792727}),
     ('Indianapolis, IN', {'location': (-86, 39), 'population': 843393}),
     ('Las Vegas, NV', {'location': (-115, 36), 'population': 603488}),
     ('Detroit, MI', {'location': (-83, 42), 'population': 688701}),
     ('Nashville-Davidson, TN', {'location': (-86, 36), 'population': 634464}),
     ('Milwaukee, WI', {'location': (-87, 43), 'population': 599164}),
     ('Columbus, OH', {'location': (-82, 39), 'population': 822553}),
     ('Virginia Beach, VA', {'location': (-75, 36), 'population': 448479}),
     ('Jacksonville, FL', {'location': (-81, 30), 'population': 842583})]




```python
# Initialize the dataframe, using the nodes as the index
df = pd.DataFrame(index=G.nodes())
```

### Extracting attributes

Using `nx.get_node_attributes` it's easy to extract the node attributes in the graph into DataFrame columns.


```python
df['location'] = pd.Series(nx.get_node_attributes(G, 'location'))
df['population'] = pd.Series(nx.get_node_attributes(G, 'population'))

df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>location</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>El Paso, TX</th>
      <td>(-106, 31)</td>
      <td>674433</td>
    </tr>
    <tr>
      <th>Long Beach, CA</th>
      <td>(-118, 33)</td>
      <td>469428</td>
    </tr>
    <tr>
      <th>Dallas, TX</th>
      <td>(-96, 32)</td>
      <td>1257676</td>
    </tr>
    <tr>
      <th>Oakland, CA</th>
      <td>(-122, 37)</td>
      <td>406253</td>
    </tr>
    <tr>
      <th>Albuquerque, NM</th>
      <td>(-106, 35)</td>
      <td>556495</td>
    </tr>
  </tbody>
</table>
</div>



### Creating node based features

Most of the networkx functions related to nodes return a dictionary, which can also easily be added to our dataframe.


```python
df['clustering'] = pd.Series(nx.clustering(G))
df['degree'] = pd.Series(G.degree())

df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>location</th>
      <th>population</th>
      <th>clustering</th>
      <th>degree</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>El Paso, TX</th>
      <td>(-106, 31)</td>
      <td>674433</td>
      <td>0.700000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Long Beach, CA</th>
      <td>(-118, 33)</td>
      <td>469428</td>
      <td>0.745455</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Dallas, TX</th>
      <td>(-96, 32)</td>
      <td>1257676</td>
      <td>0.763636</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Oakland, CA</th>
      <td>(-122, 37)</td>
      <td>406253</td>
      <td>1.000000</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Albuquerque, NM</th>
      <td>(-106, 35)</td>
      <td>556495</td>
      <td>0.523810</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Baltimore, MD</th>
      <td>(-76, 39)</td>
      <td>622104</td>
      <td>0.800000</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Raleigh, NC</th>
      <td>(-78, 35)</td>
      <td>431746</td>
      <td>0.615385</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Mesa, AZ</th>
      <td>(-111, 33)</td>
      <td>457587</td>
      <td>0.750000</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Arlington, TX</th>
      <td>(-97, 32)</td>
      <td>379577</td>
      <td>0.763636</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Sacramento, CA</th>
      <td>(-121, 38)</td>
      <td>479686</td>
      <td>0.777778</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Wichita, KS</th>
      <td>(-97, 37)</td>
      <td>386552</td>
      <td>0.622222</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Tucson, AZ</th>
      <td>(-110, 32)</td>
      <td>526116</td>
      <td>0.750000</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Cleveland, OH</th>
      <td>(-81, 41)</td>
      <td>390113</td>
      <td>0.659341</td>
      <td>14</td>
    </tr>
    <tr>
      <th>Louisville/Jefferson County, KY</th>
      <td>(-85, 38)</td>
      <td>609893</td>
      <td>0.641026</td>
      <td>13</td>
    </tr>
    <tr>
      <th>San Jose, CA</th>
      <td>(-121, 37)</td>
      <td>998537</td>
      <td>1.000000</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Oklahoma City, OK</th>
      <td>(-97, 35)</td>
      <td>610613</td>
      <td>0.636364</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Atlanta, GA</th>
      <td>(-84, 33)</td>
      <td>447841</td>
      <td>0.611111</td>
      <td>9</td>
    </tr>
    <tr>
      <th>New Orleans, LA</th>
      <td>(-90, 29)</td>
      <td>378715</td>
      <td>0.607143</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Miami, FL</th>
      <td>(-80, 25)</td>
      <td>417650</td>
      <td>0.000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Fresno, CA</th>
      <td>(-119, 36)</td>
      <td>509924</td>
      <td>0.888889</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Philadelphia, PA</th>
      <td>(-75, 39)</td>
      <td>1553165</td>
      <td>0.800000</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Houston, TX</th>
      <td>(-95, 29)</td>
      <td>2195914</td>
      <td>0.861111</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Boston, MA</th>
      <td>(-71, 42)</td>
      <td>645966</td>
      <td>1.000000</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Kansas City, MO</th>
      <td>(-94, 39)</td>
      <td>467007</td>
      <td>0.472527</td>
      <td>14</td>
    </tr>
    <tr>
      <th>San Diego, CA</th>
      <td>(-117, 32)</td>
      <td>1355896</td>
      <td>0.745455</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Chicago, IL</th>
      <td>(-87, 41)</td>
      <td>2718782</td>
      <td>0.618182</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Charlotte, NC</th>
      <td>(-80, 35)</td>
      <td>792862</td>
      <td>0.636364</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Washington D.C.</th>
      <td>(-77, 38)</td>
      <td>646449</td>
      <td>0.712121</td>
      <td>12</td>
    </tr>
    <tr>
      <th>San Antonio, TX</th>
      <td>(-98, 29)</td>
      <td>1409019</td>
      <td>1.000000</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Phoenix, AZ</th>
      <td>(-112, 33)</td>
      <td>1513367</td>
      <td>0.694444</td>
      <td>9</td>
    </tr>
    <tr>
      <th>San Francisco, CA</th>
      <td>(-122, 37)</td>
      <td>837442</td>
      <td>1.000000</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Memphis, TN</th>
      <td>(-90, 35)</td>
      <td>653450</td>
      <td>0.494505</td>
      <td>14</td>
    </tr>
    <tr>
      <th>Los Angeles, CA</th>
      <td>(-118, 34)</td>
      <td>3884307</td>
      <td>0.745455</td>
      <td>11</td>
    </tr>
    <tr>
      <th>New York, NY</th>
      <td>(-74, 40)</td>
      <td>8405837</td>
      <td>0.833333</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Denver, CO</th>
      <td>(-104, 39)</td>
      <td>649495</td>
      <td>0.666667</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Omaha, NE</th>
      <td>(-95, 41)</td>
      <td>434353</td>
      <td>0.444444</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Seattle, WA</th>
      <td>(-122, 47)</td>
      <td>652405</td>
      <td>0.000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Portland, OR</th>
      <td>(-122, 45)</td>
      <td>609456</td>
      <td>0.000000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Tulsa, OK</th>
      <td>(-95, 36)</td>
      <td>398121</td>
      <td>0.727273</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Austin, TX</th>
      <td>(-97, 30)</td>
      <td>885400</td>
      <td>0.892857</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Minneapolis, MN</th>
      <td>(-93, 44)</td>
      <td>400070</td>
      <td>1.000000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Colorado Springs, CO</th>
      <td>(-104, 38)</td>
      <td>439886</td>
      <td>0.466667</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Fort Worth, TX</th>
      <td>(-97, 32)</td>
      <td>792727</td>
      <td>0.763636</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Indianapolis, IN</th>
      <td>(-86, 39)</td>
      <td>843393</td>
      <td>0.641026</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Las Vegas, NV</th>
      <td>(-115, 36)</td>
      <td>603488</td>
      <td>0.666667</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Detroit, MI</th>
      <td>(-83, 42)</td>
      <td>688701</td>
      <td>0.672727</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Nashville-Davidson, TN</th>
      <td>(-86, 36)</td>
      <td>634464</td>
      <td>0.589744</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Milwaukee, WI</th>
      <td>(-87, 43)</td>
      <td>599164</td>
      <td>0.666667</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Columbus, OH</th>
      <td>(-82, 39)</td>
      <td>822553</td>
      <td>0.619048</td>
      <td>15</td>
    </tr>
    <tr>
      <th>Virginia Beach, VA</th>
      <td>(-75, 36)</td>
      <td>448479</td>
      <td>0.861111</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Jacksonville, FL</th>
      <td>(-81, 30)</td>
      <td>842583</td>
      <td>0.500000</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



# Edge based features


```python
G.edges(data=True)
```




    [('El Paso, TX', 'Albuquerque, NM', {'weight': 367.88584356108345}),
     ('El Paso, TX', 'Mesa, AZ', {'weight': 536.256659972679}),
     ('El Paso, TX', 'Tucson, AZ', {'weight': 425.41386739988224}),
     ('El Paso, TX', 'Phoenix, AZ', {'weight': 558.7835703774161}),
     ('El Paso, TX', 'Colorado Springs, CO', {'weight': 797.7517116740046}),
     ('Long Beach, CA', 'Oakland, CA', {'weight': 579.5829987228403}),
     ('Long Beach, CA', 'Mesa, AZ', {'weight': 590.156204210031}),
     ('Long Beach, CA', 'Sacramento, CA', {'weight': 611.0649790490104}),
     ('Long Beach, CA', 'Tucson, AZ', {'weight': 698.6566667728368}),
     ('Long Beach, CA', 'San Jose, CA', {'weight': 518.2330606219175}),
     ('Long Beach, CA', 'Fresno, CA', {'weight': 360.4704577972272}),
     ('Long Beach, CA', 'San Diego, CA', {'weight': 151.45008247402757}),
     ('Long Beach, CA', 'Phoenix, AZ', {'weight': 567.4125390872786}),
     ('Long Beach, CA', 'San Francisco, CA', {'weight': 585.6985397766858}),
     ('Long Beach, CA', 'Los Angeles, CA', {'weight': 31.69419563651866}),
     ('Long Beach, CA', 'Las Vegas, NV', {'weight': 385.2597725411484}),
     ('Dallas, TX', 'Arlington, TX', {'weight': 29.425931317908415}),
     ('Dallas, TX', 'Wichita, KS', {'weight': 548.0572491959326}),
     ('Dallas, TX', 'Oklahoma City, OK', {'weight': 306.2597807397289}),
     ('Dallas, TX', 'New Orleans, LA', {'weight': 711.0141469371868}),
     ('Dallas, TX', 'Houston, TX', {'weight': 361.54185907832755}),
     ('Dallas, TX', 'Kansas City, MO', {'weight': 730.377587942699}),
     ('Dallas, TX', 'San Antonio, TX', {'weight': 406.0065656782324}),
     ('Dallas, TX', 'Memphis, TN', {'weight': 675.3316242841653}),
     ('Dallas, TX', 'Tulsa, OK', {'weight': 382.46410800205336}),
     ('Dallas, TX', 'Austin, TX', {'weight': 292.91146634693376}),
     ('Dallas, TX', 'Fort Worth, TX', {'weight': 49.93359898977102}),
     ('Oakland, CA', 'Sacramento, CA', {'weight': 109.82159793013636}),
     ('Oakland, CA', 'San Jose, CA', {'weight': 61.90292319070633}),
     ('Oakland, CA', 'Fresno, CA', {'weight': 250.2309725980516}),
     ('Oakland, CA', 'San Diego, CA', {'weight': 730.9953136286227}),
     ('Oakland, CA', 'San Francisco, CA', {'weight': 13.428080525235567}),
     ('Oakland, CA', 'Los Angeles, CA', {'weight': 552.3121684216721}),
     ('Oakland, CA', 'Las Vegas, NV', {'weight': 658.3408716278288}),
     ('Albuquerque, NM', 'Mesa, AZ', {'weight': 514.5675468665884}),
     ('Albuquerque, NM', 'Tucson, AZ', {'weight': 510.7965704802782}),
     ('Albuquerque, NM', 'Phoenix, AZ', {'weight': 534.0407586326625}),
     ('Albuquerque, NM', 'Denver, CO', {'weight': 536.4291827646916}),
     ('Albuquerque, NM', 'Colorado Springs, CO', {'weight': 445.6400042319895}),
     ('Albuquerque, NM', 'Las Vegas, NV', {'weight': 779.953416852203}),
     ('Baltimore, MD', 'Raleigh, NC', {'weight': 429.0122832219615}),
     ('Baltimore, MD', 'Cleveland, OH', {'weight': 495.1075478023953}),
     ('Baltimore, MD', 'Philadelphia, PA', {'weight': 144.0640481858552}),
     ('Baltimore, MD', 'Boston, MA', {'weight': 578.0875135253946}),
     ('Baltimore, MD', 'Charlotte, NC', {'weight': 586.2855475627688}),
     ('Baltimore, MD', 'Washington D.C.', {'weight': 56.16567491112449}),
     ('Baltimore, MD', 'New York, NY', {'weight': 272.38422181145063}),
     ('Baltimore, MD', 'Detroit, MI', {'weight': 637.6886783148906}),
     ('Baltimore, MD', 'Columbus, OH', {'weight': 551.5744271908803}),
     ('Baltimore, MD', 'Virginia Beach, VA', {'weight': 276.4842802839367}),
     ('Raleigh, NC', 'Cleveland, OH', {'weight': 688.6125090133806}),
     ('Raleigh, NC',
      'Louisville/Jefferson County, KY',
      {'weight': 688.7073656910881}),
     ('Raleigh, NC', 'Atlanta, GA', {'weight': 571.2185028690484}),
     ('Raleigh, NC', 'Philadelphia, PA', {'weight': 554.7433742861185}),
     ('Raleigh, NC', 'Charlotte, NC', {'weight': 208.69979892270072}),
     ('Raleigh, NC', 'Washington D.C.', {'weight': 375.22530610803875}),
     ('Raleigh, NC', 'New York, NY', {'weight': 680.9077807661519}),
     ('Raleigh, NC', 'Indianapolis, IN', {'weight': 795.0096232862684}),
     ('Raleigh, NC', 'Nashville-Davidson, TN', {'weight': 733.3988290802547}),
     ('Raleigh, NC', 'Columbus, OH', {'weight': 601.698772359296}),
     ('Raleigh, NC', 'Virginia Beach, VA', {'weight': 266.37385856851193}),
     ('Raleigh, NC', 'Jacksonville, FL', {'weight': 667.2967757561717}),
     ('Mesa, AZ', 'Tucson, AZ', {'weight': 157.26017307785148}),
     ('Mesa, AZ', 'San Diego, CA', {'weight': 502.32635614606744}),
     ('Mesa, AZ', 'Phoenix, AZ', {'weight': 22.79553039579591}),
     ('Mesa, AZ', 'Los Angeles, CA', {'weight': 596.6944422568216}),
     ('Mesa, AZ', 'Las Vegas, NV', {'weight': 429.8988310173471}),
     ('Arlington, TX', 'Wichita, KS', {'weight': 550.8138003458517}),
     ('Arlington, TX', 'Oklahoma City, OK', {'weight': 305.89535561943643}),
     ('Arlington, TX', 'New Orleans, LA', {'weight': 735.8026229506348}),
     ('Arlington, TX', 'Houston, TX', {'weight': 369.5566420759369}),
     ('Arlington, TX', 'Kansas City, MO', {'weight': 742.8459954761595}),
     ('Arlington, TX', 'San Antonio, TX', {'weight': 390.8981857027806}),
     ('Arlington, TX', 'Memphis, TN', {'weight': 703.6616239985909}),
     ('Arlington, TX', 'Tulsa, OK', {'weight': 393.3587398321102}),
     ('Arlington, TX', 'Austin, TX', {'weight': 280.8343387749554}),
     ('Arlington, TX', 'Fort Worth, TX', {'weight': 20.930696675141498}),
     ('Sacramento, CA', 'San Jose, CA', {'weight': 142.37168354889943}),
     ('Sacramento, CA', 'Fresno, CA', {'weight': 253.9761318839872}),
     ('Sacramento, CA', 'San Diego, CA', {'weight': 760.0327691692984}),
     ('Sacramento, CA', 'San Francisco, CA', {'weight': 120.68134676034228}),
     ('Sacramento, CA', 'Los Angeles, CA', {'weight': 581.3180718925387}),
     ('Sacramento, CA', 'Portland, OR', {'weight': 777.4903265797615}),
     ('Sacramento, CA', 'Las Vegas, NV', {'weight': 621.6693471839634}),
     ('Wichita, KS', 'Oklahoma City, OK', {'weight': 247.36915356065145}),
     ('Wichita, KS', 'Kansas City, MO', {'weight': 286.7887192519942}),
     ('Wichita, KS', 'Memphis, TN', {'weight': 709.8334440883956}),
     ('Wichita, KS', 'Denver, CO', {'weight': 701.4183354835055}),
     ('Wichita, KS', 'Omaha, NE', {'weight': 412.2771985083082}),
     ('Wichita, KS', 'Tulsa, OK', {'weight': 208.1658493855318}),
     ('Wichita, KS', 'Colorado Springs, CO', {'weight': 665.1967107484711}),
     ('Wichita, KS', 'Fort Worth, TX', {'weight': 548.2249270170437}),
     ('Tucson, AZ', 'San Diego, CA', {'weight': 587.0077247254917}),
     ('Tucson, AZ', 'Phoenix, AZ', {'weight': 173.37868185485377}),
     ('Tucson, AZ', 'Los Angeles, CA', {'weight': 710.4231699340471}),
     ('Tucson, AZ', 'Las Vegas, NV', {'weight': 585.0709975647242}),
     ('Cleveland, OH',
      'Louisville/Jefferson County, KY',
      {'weight': 500.1707647725783}),
     ('Cleveland, OH', 'Philadelphia, PA', {'weight': 575.9173040784142}),
     ('Cleveland, OH', 'Chicago, IL', {'weight': 494.246407377749}),
     ('Cleveland, OH', 'Charlotte, NC', {'weight': 700.9265025725867}),
     ('Cleveland, OH', 'Washington D.C.', {'weight': 488.9898877488932}),
     ('Cleveland, OH', 'New York, NY', {'weight': 649.4502672715655}),
     ('Cleveland, OH', 'Indianapolis, IN', {'weight': 422.649765785015}),
     ('Cleveland, OH', 'Detroit, MI', {'weight': 145.0420206213353}),
     ('Cleveland, OH', 'Nashville-Davidson, TN', {'weight': 738.354383567491}),
     ('Cleveland, OH', 'Milwaukee, WI', {'weight': 538.5642098043521}),
     ('Cleveland, OH', 'Columbus, OH', {'weight': 203.17328268011585}),
     ('Cleveland, OH', 'Virginia Beach, VA', {'weight': 713.1719915722457}),
     ('Louisville/Jefferson County, KY',
      'Atlanta, GA',
      {'weight': 515.3935693632964}),
     ('Louisville/Jefferson County, KY',
      'Kansas City, MO',
      {'weight': 770.6369007007506}),
     ('Louisville/Jefferson County, KY',
      'Chicago, IL',
      {'weight': 433.14201586073085}),
     ('Louisville/Jefferson County, KY',
      'Charlotte, NC',
      {'weight': 551.7938053643243}),
     ('Louisville/Jefferson County, KY',
      'Washington D.C.',
      {'weight': 760.8391296292245}),
     ('Louisville/Jefferson County, KY',
      'Memphis, TN',
      {'weight': 514.7054394176082}),
     ('Louisville/Jefferson County, KY',
      'Indianapolis, IN',
      {'weight': 171.93402850524834}),
     ('Louisville/Jefferson County, KY',
      'Detroit, MI',
      {'weight': 508.16604231921934}),
     ('Louisville/Jefferson County, KY',
      'Nashville-Davidson, TN',
      {'weight': 249.27549074119767}),
     ('Louisville/Jefferson County, KY',
      'Milwaukee, WI',
      {'weight': 561.8059932331587}),
     ('Louisville/Jefferson County, KY',
      'Columbus, OH',
      {'weight': 304.39564005336484}),
     ('San Jose, CA', 'Fresno, CA', {'weight': 198.66400315450576}),
     ('San Jose, CA', 'San Diego, CA', {'weight': 669.6772910512424}),
     ('San Jose, CA', 'San Francisco, CA', {'weight': 67.53245690690382}),
     ('San Jose, CA', 'Los Angeles, CA', {'weight': 491.244577392781}),
     ('San Jose, CA', 'Las Vegas, NV', {'weight': 614.3930568650861}),
     ('Oklahoma City, OK', 'Houston, TX', {'weight': 665.217514913665}),
     ('Oklahoma City, OK', 'Kansas City, MO', {'weight': 479.91486422643885}),
     ('Oklahoma City, OK', 'San Antonio, TX', {'weight': 677.788567153514}),
     ('Oklahoma City, OK', 'Memphis, TN', {'weight': 677.9358508494545}),
     ('Oklahoma City, OK', 'Omaha, NE', {'weight': 656.2791186480706}),
     ('Oklahoma City, OK', 'Tulsa, OK', {'weight': 157.06950410857905}),
     ('Oklahoma City, OK', 'Austin, TX', {'weight': 578.2822601911338}),
     ('Oklahoma City, OK', 'Colorado Springs, CO', {'weight': 747.014568661214}),
     ('Oklahoma City, OK', 'Fort Worth, TX', {'weight': 301.86279118630887}),
     ('Atlanta, GA', 'New Orleans, LA', {'weight': 682.384954857707}),
     ('Atlanta, GA', 'Charlotte, NC', {'weight': 363.83612586974465}),
     ('Atlanta, GA', 'Memphis, TN', {'weight': 541.5047877131989}),
     ('Atlanta, GA', 'Indianapolis, IN', {'weight': 687.1751452631671}),
     ('Atlanta, GA', 'Nashville-Davidson, TN', {'weight': 345.6125153590445}),
     ('Atlanta, GA', 'Columbus, OH', {'weight': 701.2644982560505}),
     ('Atlanta, GA', 'Jacksonville, FL', {'weight': 458.65574177422604}),
     ('New Orleans, LA', 'Houston, TX', {'weight': 511.02384244889754}),
     ('New Orleans, LA', 'Memphis, TN', {'weight': 577.6842584479515}),
     ('New Orleans, LA', 'Austin, TX', {'weight': 738.1686404349225}),
     ('New Orleans, LA', 'Fort Worth, TX', {'weight': 755.8533393744848}),
     ('New Orleans, LA', 'Nashville-Davidson, TN', {'weight': 755.0752949754904}),
     ('Miami, FL', 'Jacksonville, FL', {'weight': 527.7797119911229}),
     ('Fresno, CA', 'San Diego, CA', {'weight': 507.4313769710358}),
     ('Fresno, CA', 'Phoenix, AZ', {'weight': 789.7484331199684}),
     ('Fresno, CA', 'San Francisco, CA', {'weight': 260.46960973345125}),
     ('Fresno, CA', 'Los Angeles, CA', {'weight': 329.89973534387246}),
     ('Fresno, CA', 'Las Vegas, NV', {'weight': 418.94992726715964}),
     ('Philadelphia, PA', 'Boston, MA', {'weight': 435.35607915456563}),
     ('Philadelphia, PA', 'Charlotte, NC', {'weight': 724.7428432701282}),
     ('Philadelphia, PA', 'Washington D.C.', {'weight': 198.24371380666594}),
     ('Philadelphia, PA', 'New York, NY', {'weight': 129.53654818016477}),
     ('Philadelphia, PA', 'Detroit, MI', {'weight': 710.1462898578072}),
     ('Philadelphia, PA', 'Columbus, OH', {'weight': 667.0538288622043}),
     ('Philadelphia, PA', 'Virginia Beach, VA', {'weight': 351.6415980651635}),
     ('Houston, TX', 'San Antonio, TX', {'weight': 304.1503947555647}),
     ('Houston, TX', 'Memphis, TN', {'weight': 779.1727315480448}),
     ('Houston, TX', 'Tulsa, OK', {'weight': 712.8495434682451}),
     ('Houston, TX', 'Austin, TX', {'weight': 235.1985112721572}),
     ('Houston, TX', 'Fort Worth, TX', {'weight': 381.3872407940769}),
     ('Boston, MA', 'Washington D.C.', {'weight': 633.2724255670316}),
     ('Boston, MA', 'New York, NY', {'weight': 305.91369197099885}),
     ('Boston, MA', 'Virginia Beach, VA', {'weight': 742.5833491609084}),
     ('Kansas City, MO', 'Chicago, IL', {'weight': 663.1871353165795}),
     ('Kansas City, MO', 'Memphis, TN', {'weight': 594.6054291939741}),
     ('Kansas City, MO', 'Omaha, NE', {'weight': 267.84598679216094}),
     ('Kansas City, MO', 'Tulsa, OK', {'weight': 350.19665468058116}),
     ('Kansas City, MO', 'Minneapolis, MN', {'weight': 662.1046217957743}),
     ('Kansas City, MO', 'Fort Worth, TX', {'weight': 747.1268740996313}),
     ('Kansas City, MO', 'Indianapolis, IN', {'weight': 726.2520742478256}),
     ('Kansas City, MO', 'Nashville-Davidson, TN', {'weight': 759.4820459793341}),
     ('Kansas City, MO', 'Milwaukee, WI', {'weight': 709.5921370123627}),
     ('San Diego, CA', 'Phoenix, AZ', {'weight': 480.550984974869}),
     ('San Diego, CA', 'San Francisco, CA', {'weight': 737.1473892523547}),
     ('San Diego, CA', 'Los Angeles, CA', {'weight': 179.29746717246732}),
     ('San Diego, CA', 'Las Vegas, NV', {'weight': 426.17584242277843}),
     ('Chicago, IL', 'Memphis, TN', {'weight': 776.6422940993197}),
     ('Chicago, IL', 'Omaha, NE', {'weight': 698.9473960021885}),
     ('Chicago, IL', 'Minneapolis, MN', {'weight': 570.2677332774025}),
     ('Chicago, IL', 'Indianapolis, IN', {'weight': 265.0916992417503}),
     ('Chicago, IL', 'Detroit, MI', {'weight': 381.2299668022458}),
     ('Chicago, IL', 'Nashville-Davidson, TN', {'weight': 639.3273291549567}),
     ('Chicago, IL', 'Milwaukee, WI', {'weight': 130.97175617954392}),
     ('Chicago, IL', 'Columbus, OH', {'weight': 443.294756640302}),
     ('Charlotte, NC', 'Washington D.C.', {'weight': 530.1200050223144}),
     ('Charlotte, NC', 'Indianapolis, IN', {'weight': 688.3846733430148}),
     ('Charlotte, NC', 'Nashville-Davidson, TN', {'weight': 545.8353443886101}),
     ('Charlotte, NC', 'Columbus, OH', {'weight': 559.2175271096321}),
     ('Charlotte, NC', 'Virginia Beach, VA', {'weight': 472.95036855569816}),
     ('Charlotte, NC', 'Jacksonville, FL', {'weight': 549.2112199489682}),
     ('Washington D.C.', 'New York, NY', {'weight': 327.37847523720734}),
     ('Washington D.C.', 'Indianapolis, IN', {'weight': 789.4034447188161}),
     ('Washington D.C.', 'Detroit, MI', {'weight': 633.5169854294026}),
     ('Washington D.C.', 'Columbus, OH', {'weight': 524.8211194461829}),
     ('Washington D.C.', 'Virginia Beach, VA', {'weight': 246.445149222362}),
     ('San Antonio, TX', 'Tulsa, OK', {'weight': 783.407957742418}),
     ('San Antonio, TX', 'Austin, TX', {'weight': 118.36314806535839}),
     ('San Antonio, TX', 'Fort Worth, TX', {'weight': 386.37486866810514}),
     ('Phoenix, AZ', 'Los Angeles, CA', {'weight': 573.9011736942347}),
     ('Phoenix, AZ', 'Las Vegas, NV', {'weight': 411.9094912462262}),
     ('San Francisco, CA', 'Los Angeles, CA', {'weight': 558.7708978607576}),
     ('San Francisco, CA', 'Las Vegas, NV', {'weight': 670.2380164875032}),
     ('Memphis, TN', 'Tulsa, OK', {'weight': 548.09611297848}),
     ('Memphis, TN', 'Fort Worth, TX', {'weight': 721.7845495553929}),
     ('Memphis, TN', 'Indianapolis, IN', {'weight': 617.295220276267}),
     ('Memphis, TN', 'Nashville-Davidson, TN', {'weight': 315.75011030810685}),
     ('Los Angeles, CA', 'Las Vegas, NV', {'weight': 367.37280090555305}),
     ('New York, NY', 'Detroit, MI', {'weight': 772.9011410671837}),
     ('New York, NY', 'Columbus, OH', {'weight': 765.9634514216572}),
     ('New York, NY', 'Virginia Beach, VA', {'weight': 461.65690712679395}),
     ('Denver, CO', 'Omaha, NE', {'weight': 777.8863249384502}),
     ('Denver, CO', 'Colorado Springs, CO', {'weight': 101.65075926223551}),
     ('Omaha, NE', 'Tulsa, OK', {'weight': 566.5584360997123}),
     ('Omaha, NE', 'Minneapolis, MN', {'weight': 469.53764600116483}),
     ('Omaha, NE', 'Colorado Springs, CO', {'weight': 796.8394903997096}),
     ('Omaha, NE', 'Milwaukee, WI', {'weight': 695.28556620892}),
     ('Seattle, WA', 'Portland, OR', {'weight': 232.98003496425403}),
     ('Tulsa, OK', 'Austin, TX', {'weight': 674.071176589555}),
     ('Tulsa, OK', 'Fort Worth, TX', {'weight': 397.0462555225492}),
     ('Austin, TX', 'Fort Worth, TX', {'weight': 279.2607716124542}),
     ('Minneapolis, MN', 'Milwaukee, WI', {'weight': 479.28775968088723}),
     ('Indianapolis, IN', 'Detroit, MI', {'weight': 386.1408406535182}),
     ('Indianapolis, IN', 'Nashville-Davidson, TN', {'weight': 404.3913216129687}),
     ('Indianapolis, IN', 'Milwaukee, WI', {'weight': 391.5388446310555}),
     ('Indianapolis, IN', 'Columbus, OH', {'weight': 270.3063479826381}),
     ('Detroit, MI', 'Milwaukee, WI', {'weight': 404.7034896583142}),
     ('Detroit, MI', 'Nashville-Davidson, TN', {'weight': 756.943864661379}),
     ('Detroit, MI', 'Columbus, OH', {'weight': 263.423764720247}),
     ('Nashville-Davidson, TN', 'Milwaukee, WI', {'weight': 770.1467064269982}),
     ('Nashville-Davidson, TN', 'Columbus, OH', {'weight': 536.2745483969072}),
     ('Milwaukee, WI', 'Columbus, OH', {'weight': 532.5684227398444}),
     ('Columbus, OH', 'Virginia Beach, VA', {'weight': 701.8766661783677})]




```python
# Initialize the dataframe, using the edges as the index
df = pd.DataFrame(index=G.edges())
```

### Extracting attributes

Using `nx.get_edge_attributes`, it's easy to extract the edge attributes in the graph into DataFrame columns.


```python
df['weight'] = pd.Series(nx.get_edge_attributes(G, 'weight'))

df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(El Paso, TX, Albuquerque, NM)</th>
      <td>367.885844</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Mesa, AZ)</th>
      <td>536.256660</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Tucson, AZ)</th>
      <td>425.413867</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Phoenix, AZ)</th>
      <td>558.783570</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Colorado Springs, CO)</th>
      <td>797.751712</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Oakland, CA)</th>
      <td>579.582999</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Mesa, AZ)</th>
      <td>590.156204</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Sacramento, CA)</th>
      <td>611.064979</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Tucson, AZ)</th>
      <td>698.656667</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Jose, CA)</th>
      <td>518.233061</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Fresno, CA)</th>
      <td>360.470458</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Diego, CA)</th>
      <td>151.450082</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Phoenix, AZ)</th>
      <td>567.412539</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Francisco, CA)</th>
      <td>585.698540</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Los Angeles, CA)</th>
      <td>31.694196</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Las Vegas, NV)</th>
      <td>385.259773</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Arlington, TX)</th>
      <td>29.425931</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Wichita, KS)</th>
      <td>548.057249</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Oklahoma City, OK)</th>
      <td>306.259781</td>
    </tr>
    <tr>
      <th>(Dallas, TX, New Orleans, LA)</th>
      <td>711.014147</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Houston, TX)</th>
      <td>361.541859</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Kansas City, MO)</th>
      <td>730.377588</td>
    </tr>
    <tr>
      <th>(Dallas, TX, San Antonio, TX)</th>
      <td>406.006566</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Memphis, TN)</th>
      <td>675.331624</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Tulsa, OK)</th>
      <td>382.464108</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Austin, TX)</th>
      <td>292.911466</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Fort Worth, TX)</th>
      <td>49.933599</td>
    </tr>
    <tr>
      <th>(Oakland, CA, Sacramento, CA)</th>
      <td>109.821598</td>
    </tr>
    <tr>
      <th>(Oakland, CA, San Jose, CA)</th>
      <td>61.902923</td>
    </tr>
    <tr>
      <th>(Oakland, CA, Fresno, CA)</th>
      <td>250.230973</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Tulsa, OK)</th>
      <td>548.096113</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Fort Worth, TX)</th>
      <td>721.784550</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Indianapolis, IN)</th>
      <td>617.295220</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Nashville-Davidson, TN)</th>
      <td>315.750110</td>
    </tr>
    <tr>
      <th>(Los Angeles, CA, Las Vegas, NV)</th>
      <td>367.372801</td>
    </tr>
    <tr>
      <th>(New York, NY, Detroit, MI)</th>
      <td>772.901141</td>
    </tr>
    <tr>
      <th>(New York, NY, Columbus, OH)</th>
      <td>765.963451</td>
    </tr>
    <tr>
      <th>(New York, NY, Virginia Beach, VA)</th>
      <td>461.656907</td>
    </tr>
    <tr>
      <th>(Denver, CO, Omaha, NE)</th>
      <td>777.886325</td>
    </tr>
    <tr>
      <th>(Denver, CO, Colorado Springs, CO)</th>
      <td>101.650759</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Tulsa, OK)</th>
      <td>566.558436</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Minneapolis, MN)</th>
      <td>469.537646</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Colorado Springs, CO)</th>
      <td>796.839490</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Milwaukee, WI)</th>
      <td>695.285566</td>
    </tr>
    <tr>
      <th>(Seattle, WA, Portland, OR)</th>
      <td>232.980035</td>
    </tr>
    <tr>
      <th>(Tulsa, OK, Austin, TX)</th>
      <td>674.071177</td>
    </tr>
    <tr>
      <th>(Tulsa, OK, Fort Worth, TX)</th>
      <td>397.046256</td>
    </tr>
    <tr>
      <th>(Austin, TX, Fort Worth, TX)</th>
      <td>279.260772</td>
    </tr>
    <tr>
      <th>(Minneapolis, MN, Milwaukee, WI)</th>
      <td>479.287760</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Detroit, MI)</th>
      <td>386.140841</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Nashville-Davidson, TN)</th>
      <td>404.391322</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Milwaukee, WI)</th>
      <td>391.538845</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Columbus, OH)</th>
      <td>270.306348</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Milwaukee, WI)</th>
      <td>404.703490</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Nashville-Davidson, TN)</th>
      <td>756.943865</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Columbus, OH)</th>
      <td>263.423765</td>
    </tr>
    <tr>
      <th>(Nashville-Davidson, TN, Milwaukee, WI)</th>
      <td>770.146706</td>
    </tr>
    <tr>
      <th>(Nashville-Davidson, TN, Columbus, OH)</th>
      <td>536.274548</td>
    </tr>
    <tr>
      <th>(Milwaukee, WI, Columbus, OH)</th>
      <td>532.568423</td>
    </tr>
    <tr>
      <th>(Columbus, OH, Virginia Beach, VA)</th>
      <td>701.876666</td>
    </tr>
  </tbody>
</table>
<p>235 rows × 1 columns</p>
</div>



### Creating edge based features

Many of the networkx functions related to edges return a nested data structures. We can extract the relevant data using list comprehension.


```python
df['preferential attachment'] = [i[2] for i in nx.preferential_attachment(G, df.index)]

df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>weight</th>
      <th>preferential attachment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(El Paso, TX, Albuquerque, NM)</th>
      <td>367.885844</td>
      <td>35</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Mesa, AZ)</th>
      <td>536.256660</td>
      <td>40</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Tucson, AZ)</th>
      <td>425.413867</td>
      <td>40</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Phoenix, AZ)</th>
      <td>558.783570</td>
      <td>45</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Colorado Springs, CO)</th>
      <td>797.751712</td>
      <td>30</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Oakland, CA)</th>
      <td>579.582999</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Mesa, AZ)</th>
      <td>590.156204</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Sacramento, CA)</th>
      <td>611.064979</td>
      <td>99</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Tucson, AZ)</th>
      <td>698.656667</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Jose, CA)</th>
      <td>518.233061</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Fresno, CA)</th>
      <td>360.470458</td>
      <td>99</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Diego, CA)</th>
      <td>151.450082</td>
      <td>121</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Phoenix, AZ)</th>
      <td>567.412539</td>
      <td>99</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Francisco, CA)</th>
      <td>585.698540</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Los Angeles, CA)</th>
      <td>31.694196</td>
      <td>121</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Las Vegas, NV)</th>
      <td>385.259773</td>
      <td>132</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Arlington, TX)</th>
      <td>29.425931</td>
      <td>121</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Wichita, KS)</th>
      <td>548.057249</td>
      <td>110</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Oklahoma City, OK)</th>
      <td>306.259781</td>
      <td>132</td>
    </tr>
    <tr>
      <th>(Dallas, TX, New Orleans, LA)</th>
      <td>711.014147</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Houston, TX)</th>
      <td>361.541859</td>
      <td>99</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Kansas City, MO)</th>
      <td>730.377588</td>
      <td>154</td>
    </tr>
    <tr>
      <th>(Dallas, TX, San Antonio, TX)</th>
      <td>406.006566</td>
      <td>77</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Memphis, TN)</th>
      <td>675.331624</td>
      <td>154</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Tulsa, OK)</th>
      <td>382.464108</td>
      <td>121</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Austin, TX)</th>
      <td>292.911466</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Fort Worth, TX)</th>
      <td>49.933599</td>
      <td>121</td>
    </tr>
    <tr>
      <th>(Oakland, CA, Sacramento, CA)</th>
      <td>109.821598</td>
      <td>72</td>
    </tr>
    <tr>
      <th>(Oakland, CA, San Jose, CA)</th>
      <td>61.902923</td>
      <td>64</td>
    </tr>
    <tr>
      <th>(Oakland, CA, Fresno, CA)</th>
      <td>250.230973</td>
      <td>72</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Tulsa, OK)</th>
      <td>548.096113</td>
      <td>154</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Fort Worth, TX)</th>
      <td>721.784550</td>
      <td>154</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Indianapolis, IN)</th>
      <td>617.295220</td>
      <td>182</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Nashville-Davidson, TN)</th>
      <td>315.750110</td>
      <td>182</td>
    </tr>
    <tr>
      <th>(Los Angeles, CA, Las Vegas, NV)</th>
      <td>367.372801</td>
      <td>132</td>
    </tr>
    <tr>
      <th>(New York, NY, Detroit, MI)</th>
      <td>772.901141</td>
      <td>99</td>
    </tr>
    <tr>
      <th>(New York, NY, Columbus, OH)</th>
      <td>765.963451</td>
      <td>135</td>
    </tr>
    <tr>
      <th>(New York, NY, Virginia Beach, VA)</th>
      <td>461.656907</td>
      <td>81</td>
    </tr>
    <tr>
      <th>(Denver, CO, Omaha, NE)</th>
      <td>777.886325</td>
      <td>36</td>
    </tr>
    <tr>
      <th>(Denver, CO, Colorado Springs, CO)</th>
      <td>101.650759</td>
      <td>24</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Tulsa, OK)</th>
      <td>566.558436</td>
      <td>99</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Minneapolis, MN)</th>
      <td>469.537646</td>
      <td>36</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Colorado Springs, CO)</th>
      <td>796.839490</td>
      <td>54</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Milwaukee, WI)</th>
      <td>695.285566</td>
      <td>90</td>
    </tr>
    <tr>
      <th>(Seattle, WA, Portland, OR)</th>
      <td>232.980035</td>
      <td>2</td>
    </tr>
    <tr>
      <th>(Tulsa, OK, Austin, TX)</th>
      <td>674.071177</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Tulsa, OK, Fort Worth, TX)</th>
      <td>397.046256</td>
      <td>121</td>
    </tr>
    <tr>
      <th>(Austin, TX, Fort Worth, TX)</th>
      <td>279.260772</td>
      <td>88</td>
    </tr>
    <tr>
      <th>(Minneapolis, MN, Milwaukee, WI)</th>
      <td>479.287760</td>
      <td>40</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Detroit, MI)</th>
      <td>386.140841</td>
      <td>143</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Nashville-Davidson, TN)</th>
      <td>404.391322</td>
      <td>169</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Milwaukee, WI)</th>
      <td>391.538845</td>
      <td>130</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Columbus, OH)</th>
      <td>270.306348</td>
      <td>195</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Milwaukee, WI)</th>
      <td>404.703490</td>
      <td>110</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Nashville-Davidson, TN)</th>
      <td>756.943865</td>
      <td>143</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Columbus, OH)</th>
      <td>263.423765</td>
      <td>165</td>
    </tr>
    <tr>
      <th>(Nashville-Davidson, TN, Milwaukee, WI)</th>
      <td>770.146706</td>
      <td>130</td>
    </tr>
    <tr>
      <th>(Nashville-Davidson, TN, Columbus, OH)</th>
      <td>536.274548</td>
      <td>195</td>
    </tr>
    <tr>
      <th>(Milwaukee, WI, Columbus, OH)</th>
      <td>532.568423</td>
      <td>150</td>
    </tr>
    <tr>
      <th>(Columbus, OH, Virginia Beach, VA)</th>
      <td>701.876666</td>
      <td>135</td>
    </tr>
  </tbody>
</table>
<p>235 rows × 2 columns</p>
</div>



In the case where the function expects two nodes to be passed in, we can map the index to a lamda function.


```python
df['Common Neighbors'] = df.index.map(lambda city: len(list(nx.common_neighbors(G, city[0], city[1]))))

df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>weight</th>
      <th>preferential attachment</th>
      <th>Common Neighbors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(El Paso, TX, Albuquerque, NM)</th>
      <td>367.885844</td>
      <td>35</td>
      <td>4</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Mesa, AZ)</th>
      <td>536.256660</td>
      <td>40</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Tucson, AZ)</th>
      <td>425.413867</td>
      <td>40</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Phoenix, AZ)</th>
      <td>558.783570</td>
      <td>45</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(El Paso, TX, Colorado Springs, CO)</th>
      <td>797.751712</td>
      <td>30</td>
      <td>1</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Oakland, CA)</th>
      <td>579.582999</td>
      <td>88</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Mesa, AZ)</th>
      <td>590.156204</td>
      <td>88</td>
      <td>5</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Sacramento, CA)</th>
      <td>611.064979</td>
      <td>99</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Tucson, AZ)</th>
      <td>698.656667</td>
      <td>88</td>
      <td>5</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Jose, CA)</th>
      <td>518.233061</td>
      <td>88</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Fresno, CA)</th>
      <td>360.470458</td>
      <td>99</td>
      <td>8</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Diego, CA)</th>
      <td>151.450082</td>
      <td>121</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Phoenix, AZ)</th>
      <td>567.412539</td>
      <td>99</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, San Francisco, CA)</th>
      <td>585.698540</td>
      <td>88</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Los Angeles, CA)</th>
      <td>31.694196</td>
      <td>121</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Long Beach, CA, Las Vegas, NV)</th>
      <td>385.259773</td>
      <td>132</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Arlington, TX)</th>
      <td>29.425931</td>
      <td>121</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Wichita, KS)</th>
      <td>548.057249</td>
      <td>110</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Oklahoma City, OK)</th>
      <td>306.259781</td>
      <td>132</td>
      <td>9</td>
    </tr>
    <tr>
      <th>(Dallas, TX, New Orleans, LA)</th>
      <td>711.014147</td>
      <td>88</td>
      <td>5</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Houston, TX)</th>
      <td>361.541859</td>
      <td>99</td>
      <td>8</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Kansas City, MO)</th>
      <td>730.377588</td>
      <td>154</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Dallas, TX, San Antonio, TX)</th>
      <td>406.006566</td>
      <td>77</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Memphis, TN)</th>
      <td>675.331624</td>
      <td>154</td>
      <td>8</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Tulsa, OK)</th>
      <td>382.464108</td>
      <td>121</td>
      <td>9</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Austin, TX)</th>
      <td>292.911466</td>
      <td>88</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Dallas, TX, Fort Worth, TX)</th>
      <td>49.933599</td>
      <td>121</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Oakland, CA, Sacramento, CA)</th>
      <td>109.821598</td>
      <td>72</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Oakland, CA, San Jose, CA)</th>
      <td>61.902923</td>
      <td>64</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Oakland, CA, Fresno, CA)</th>
      <td>250.230973</td>
      <td>72</td>
      <td>7</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Tulsa, OK)</th>
      <td>548.096113</td>
      <td>154</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Fort Worth, TX)</th>
      <td>721.784550</td>
      <td>154</td>
      <td>8</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Indianapolis, IN)</th>
      <td>617.295220</td>
      <td>182</td>
      <td>5</td>
    </tr>
    <tr>
      <th>(Memphis, TN, Nashville-Davidson, TN)</th>
      <td>315.750110</td>
      <td>182</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Los Angeles, CA, Las Vegas, NV)</th>
      <td>367.372801</td>
      <td>132</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(New York, NY, Detroit, MI)</th>
      <td>772.901141</td>
      <td>99</td>
      <td>5</td>
    </tr>
    <tr>
      <th>(New York, NY, Columbus, OH)</th>
      <td>765.963451</td>
      <td>135</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(New York, NY, Virginia Beach, VA)</th>
      <td>461.656907</td>
      <td>81</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Denver, CO, Omaha, NE)</th>
      <td>777.886325</td>
      <td>36</td>
      <td>2</td>
    </tr>
    <tr>
      <th>(Denver, CO, Colorado Springs, CO)</th>
      <td>101.650759</td>
      <td>24</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Tulsa, OK)</th>
      <td>566.558436</td>
      <td>99</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Minneapolis, MN)</th>
      <td>469.537646</td>
      <td>36</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Colorado Springs, CO)</th>
      <td>796.839490</td>
      <td>54</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(Omaha, NE, Milwaukee, WI)</th>
      <td>695.285566</td>
      <td>90</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(Seattle, WA, Portland, OR)</th>
      <td>232.980035</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>(Tulsa, OK, Austin, TX)</th>
      <td>674.071177</td>
      <td>88</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Tulsa, OK, Fort Worth, TX)</th>
      <td>397.046256</td>
      <td>121</td>
      <td>9</td>
    </tr>
    <tr>
      <th>(Austin, TX, Fort Worth, TX)</th>
      <td>279.260772</td>
      <td>88</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Minneapolis, MN, Milwaukee, WI)</th>
      <td>479.287760</td>
      <td>40</td>
      <td>3</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Detroit, MI)</th>
      <td>386.140841</td>
      <td>143</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Nashville-Davidson, TN)</th>
      <td>404.391322</td>
      <td>169</td>
      <td>11</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Milwaukee, WI)</th>
      <td>391.538845</td>
      <td>130</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Indianapolis, IN, Columbus, OH)</th>
      <td>270.306348</td>
      <td>195</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Milwaukee, WI)</th>
      <td>404.703490</td>
      <td>110</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Nashville-Davidson, TN)</th>
      <td>756.943865</td>
      <td>143</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Detroit, MI, Columbus, OH)</th>
      <td>263.423765</td>
      <td>165</td>
      <td>10</td>
    </tr>
    <tr>
      <th>(Nashville-Davidson, TN, Milwaukee, WI)</th>
      <td>770.146706</td>
      <td>130</td>
      <td>7</td>
    </tr>
    <tr>
      <th>(Nashville-Davidson, TN, Columbus, OH)</th>
      <td>536.274548</td>
      <td>195</td>
      <td>9</td>
    </tr>
    <tr>
      <th>(Milwaukee, WI, Columbus, OH)</th>
      <td>532.568423</td>
      <td>150</td>
      <td>6</td>
    </tr>
    <tr>
      <th>(Columbus, OH, Virginia Beach, VA)</th>
      <td>701.876666</td>
      <td>135</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
<p>235 rows × 3 columns</p>
</div>


