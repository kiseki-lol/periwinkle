# periwinkle

Discord management bot for Kiseki instances

Package requirements:

- `discord.py`
- `python-dotenv`
- `humanize`

## Usage

Run `python periwinkle.py` to start the bot

Create a `.env` file with the following contents:

| Name         | Expected value                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TOKEN`      | Discord bot token                                                                                                                                                                  |
| `KISEKI_URL` | Kiseki root URL                                                                                                                                                                    |
| `API_KEY`    | Periwinkle API key that you generated with `sail artisan generate-periwinkle-key` ([read more](https://github.com/kiseki-lol/web/trunk/docs/api.md#periwinkle-api-key-generation)) |

## License

periwinkle is licensed under the [AGPLv3 license](https://github.com/kiseki-lol/periwinkle/blob/trunk/LICENSE.md). A copy of it has been included with periwinkle.

Banner drawn by [@briwaffles](https://twitter.com/briwaffles).
