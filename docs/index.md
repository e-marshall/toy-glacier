# Welcome to toy-glacier

This is a very small toy CLI tool.

## Commands

* `accumulation-event` - Create a glacier and trigger an accumulation event with a specified amount. 
* `ablation-event` - Create a glacier and trigger an ablation event with a specified amount. 

## Example

Call either command and pass an `amount` argument:

```
toy-glacier accumulation-event 45
```
Returns:
```
Glacier created with name: defaultName, initial volume: 100 m3.
Accumulation event: Total volume is now 145 m3.
```

By default, each command creates a glacier with a volume of 100 m3 and the name, 'defaultName'. To modify either of these default arguments, pass them as optional args:

```
toy-glacier ablation-event 15 --glacier-volume 50 -- name MyFirstGlacier
```
Returns:
```
Glacier created with name: MyFirstGlacier, initial volume: 50 m3.
Ablation event: Volume is now 35 m3.
```