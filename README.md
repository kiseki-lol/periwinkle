# periwinkle

Discord management bot for Kiseki instances

Requires:

- discord.py
- python-dotenv

## Usage

Run `python periwinkle.py` to start the bot

Create a `.env` file with the following contents:

```
TOKEN=<your discord bot token>
KISEKI_URL=<the root to your kiseki instance, e.g. http://kiseki.loc>
API_KEY=<your kiseki API key that you generated with "sail artisan generate-periwinkle-key" (see https://github.com/kiseki-lol/web/trunk/docs/api.md#periwinkle-api-key-generation)>
```

## License

periwinkle is licensed under the [AGPLv3 license](https://github.com/kiseki-lol/periwinkle/blob/trunk/LICENSE.md). A copy of it has been included with periwinkle.
