# GPT2 sherlock
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ha-mulan/gpt2-sherlock)



### Model information


    Base model: gpt-2 large
    Epoch: 20
    Loss: 0.15
    Dataset:Sherlock (https://www.kaggle.com/idevji1/sherlock-holmes-stories)
    License:CC0: Public Domain





### About
	this model is based on gpt2-large and fine tuned with sherlock script dataset.
	it generates sherlock scrip related to your input keyword.
	first, input your keyword
	second, wait for result

### How to use

	three ways to use Gpt2 sherlock
    	1.  CLI
    	2.  Swagger
    	3.  Demo

### GET parameter

    keyword: input your keyword than you will check out the sherlock script related to keyword

### Output format

    generated text


##  *With CLI*

### Input example

    curl -X GET "https://master-gpt2-sherlock-ha-mulan.endpoint.ainize.ai/api/?keyword=murder" -H "accept: string"


### Output example

        murderous outbursts and it seemed to me that
        to speak at all was very painful to him and that his will all
        through was overriding his inclinations

        it is a very delicate thing said he one does not like to speak of
        ones domestic affairs to strangers it seems dreadful to discuss the
        conduct of ones wife with two men whom i have never seen before
        it is horrible to have to do it but i have got to the end of my tether
        and i must have advice

        my dear mr grant munro began holmes

        our visitor sprang from his chair what he cried you know my
        name

        if you wish to preserve your incognito said holmes smiling i suggest that you cease to
        write your name upon the lining of your hat or else that you turn the crown
        towards the person whom you are addressing i was about to say that my friend and i
        have been expecting you come round for some months
        therefore i had no difficulty in finding you

        the doctor flushed with anger

        i have been expecting you for some time said he but you must have forgotten my advice or i was not to

## *With swagger*

API page: [Ainize](https://ainize.ai/ha-mulan/gpt2-sherlock?branch=master)

## *With a Demo*

Demo page: [End-point](https://master-gpt2-sherlock-ha-mulan.endpoint.ainize.ai)
