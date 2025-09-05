# Welcome to toy-glacier-project

This is a very small toy CLI tool.

## Commands

* `accumulation-event` :material-water-plus: - Create a glacier and trigger an accumulation event with a specified amount. 
* `ablation-event` :material-water-remove: - Create a glacier and trigger an ablation event with a specified amount. 

## Example

Call either command and pass an `amount` argument:

```
toy-glacier-project accumulation-event 45
```
Returns:
```
Glacier created with name: defaultName, initial mass: 100 kg.
Accumulation event: Total mass is now 145 kg.
```

By default, each command creates a glacier with a mass of 100 kg and the name 'defaultName'. To modify either of these default arguments, pass them as optional args:

```
toy-glacier-project ablation-event 15 --glacier-mass 50 -- name MyFirstGlacier
```
Returns:
```
Glacier created with name: MyFirstGlacier, initial mass: 50 kg.
Ablation event: Mass is now 35 kg.
```