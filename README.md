# Olist Sales Forecasting (WIP)

Small description of the project: what is the problem? How did you solve it? who would be interested in this project.

## Project DAG

```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

< INSERT PROJECT DAG HERE>

## Results

insert a gif or imgs with the project results

## Premises

For this project:

* I'll only consider orders with the 'delivered' status;
* The sale_date is considered to be equal to the order approval date;

## Tech Stack

* [DARTS](https://unit8co.github.io/darts/)
* [Pandas](https://pandas.pydata.org/docs/index.html)


List the stack used divided by module

**model_training:** Scikit-Learn, Keras

**pre_processing:** Numpy, Pandas, imblearn

## Running this project

Give clear instructions on how to run this project.

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

## Lessons

* DARTS and PyTorch work better with python 3.10
* According to Syntetos, Boylan, and Croston demand can be categorized into:

| category    | ADI     | CV2     |
| ----------- | ------- | ------- |
| smooth      | < 1.32  | < 0.49  |
| erratic     | < 1.32  | \> 0.49 |
| intermitent | \> 1.32 | < 0.49  |
| lumpy       | \> 1.32 | \> 0.49 |

* Lesson D

## References

```
 @misc{olist_andré sionek_2018,
	title={Brazilian E-Commerce Public Dataset by Olist},
	url={https://www.kaggle.com/dsv/195341},
	DOI={10.34740/KAGGLE/DSV/195341},
	publisher={Kaggle},
	author={Olist and André Sionek},
	year={2018}
}

@misc{rožanec2021reframing,
      title={Reframing demand forecasting: a two-fold approach for lumpy and intermittent demand}, 
      author={Jože M. Rožanec and Dunja Mladenić},
      year={2021},
      eprint={2103.13812},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}

@article{article,
      author = {Syntetos, M and Boylan, John and Croston, JD},
      year = {2005},
      month = {05},
      pages = {},
      title = {On the categorization of demand patterns},
      volume = {56},
      journal = {Journal of the Operational Research Society},
      doi = {10.1057/palgrave.jors.2601841}
}

```

[Solis, A.O., Nicoletti, L., Mukhopadhyay, S., Agosteo, L., Delfino, A., Sartiano, M. .Intermittent Demand Forecasting and Stock Control: An Empirical Study. Proceedings of the International Conference on Modeling and Applied Simulation 2012, 367-374](http://www.msc-les.org/proceedings/mas/2012/MAS2012_367.pdf)