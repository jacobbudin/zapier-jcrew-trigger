# Zapier J.Crew Trigger

A Zapier trigger to monitor J.Crew product availability

## Why

Let Zapier constantly refresh the product page for you and alert you when an item is in stock while you watch Netflix.

## Prerequisites

1. [A Zapier account](https://zapier.com), a free one works fine
2. An out of stock J.Crew product that you want

## Use

1. Log-in to Zapier.
2. Click "Make a New Zap".
3. As your first action, choose "Code by Zapier".
	1. Run Python
	2. Copy and paste the code in [`jcrew.py`](https://raw.githubusercontent.com/jacobbudin/zapier-jcrew-trigger/master/jcrew.py) into the code area.
		1. Modify the product ID, size, and color to match your desired item.
			- Note: The product ID is item number beneath the product's title on the product's page.
	3. Test and continue.
4. As your second action, choose "SMS by Zapier" (or an alternative method to alert you that your item is now in stock), and set it up.
5. Lastly, add a filter in between these two actions. You only want the second action to occur if and only if the item is in stock.
	1. Choose "Is Available", "(Text) Exactly Matches", and enter `true`.

If you choose the SMS action, you'll receive a message when the product becomes in stock. On free accounts, Zapier runs trigger actions once every 15 minutes, so you should be notified within 15 minutes of your item becoming available.

## Author
[Jacob Budin](http://www.jacobbudin.com)

## License
MIT License
