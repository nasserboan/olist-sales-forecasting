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
* Lesson C
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
```