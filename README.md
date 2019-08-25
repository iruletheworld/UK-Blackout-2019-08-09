# Frequency and Events of the UK Blackout on 2019-08-09

On August the 9th, 2019 (Friday) afternoon, large parts of England and Wales suffered power cuts, affecting around 1m people and causing widespread disruption to trains and roads ahead of a busy weekend for holiday travel. The power supplies to the trains were not lost, but the supplies to the signallings were.

The National Grid (UK) has released an [interim report](https://www.nationalgrideso.com/information-about-great-britains-energy-system-and-electricity-system-operator-eso) about the event.

This project uses public available frequency data and NG's report to produce an annotated frequency event plot. The frequency data is from Elexon (Rolling System Frequency).

## Frequency events on 2018-08-09
![Frequency events](./uk_blackout_2019_08_09.png)

See the "requirements.txt" for the Python dependencies.

The data used in this project are of 15 sec resolution, therefore it is necessary to perform upsampling to make the curve smoother and easier to annotate.

The demand and generation data available public are of much lower resolutions (5 min) and thus they are not plotted.

NG usually release the hirstorical frequency data (1 sec resolution) in a 4-moth window. Thus, the frequency data per second of August should be available in December. At that time, the plot could be updated using the better data.

## License

MIT

## Contributing

**高斯羽 博士** (**Dr. Gāo, Sīyǔ**)