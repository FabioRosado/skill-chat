# opsdroid skill chat

This skill adds some basic chatting abilities to [opsdroid](https://github.com/opsdroid/opsdroid).
You can also replace the default answer for every interaction with opsdroid by changing the values on your configuration.yaml.

## Requirements

None.

## Configuration

```yaml
  - name: chat
    repo: https://github.com/FabioRosado/skill-chat.git
    # Optional (Allows customisation of default answers)
#   customise: !include customise.yaml
```



## Usage

#### Tell me a joke
Opsdroid will reply from a list of jokes


> user: tell me a joke
>
> opsdroid: I'm addicted to brake fluid, but I can stop whenever I want.


#### How are you
Opsdroid will reply from a list of answers
> user: how are you
>
> opsdroid: I'm good and you?


#### What is your name
Opsdroid will tell you its name
> user: what is your name
>
> opsdroid: I'm opsdroid and I'm here to help


#### Thank you
Opsdroid will reply to you when you say thank you
> user: Thank you
>
> opsdroid: You're welcome username! :D


#### I'm sorry
Opsdroid will reply to "I'm sorry"
> user: I'm sorry
>
> opsdroid: No worries


#### Are you a robot
Opsdroid will answer to the question "are you a bot"
> user: Are you a robot
>
> opsdroid: I am a chat bot, created to help you achieve greatness!


#### How old are you
Opsdroid will tell you how old is he
> user: how old are you
>
> opsdroid: Age doesn't really matter to me, but I was created on 26 July 2016 so that makes me 2 months old


#### Where are you
Opsdroid will tell you his location
> user: where are you
>
> opsdroid: Inside your device




## License

GNU General Public License Version 3 (GPLv3)
