from typesense import Client


def create_schema(client: Client):
    reliable_articles_schema = {
        'name':
        'reliable_articles',
        'fields': [
            {
                # Just numbers
                'name': 'id',
                'type': 'string'
            },
            {},
            {
                'name': 'url',
                'type': 'string'
            },
            {
                # Title extracted by Google search
                'name': 'google_title',
                'type': 'string'
            },
            {
                # Title extracted by us
                'name': 'title',
                'type': 'string',
                'optional': True
            },
            {
                # Since this is a default sorting field, it cannot be
                # optional. Hence when not available, date is set to 0 (oldest
                # representale time). This is a UNIX timestamp
                'name': 'date',
                'type': 'int64',
            },
            {
                'name': 'description',
                'type': 'string',
                'optional': True
            },
            {
                # Extracted text from the HTML
                'name': 'text',
                'type': 'string',
                'optional': True
            },
            {
                # Full HTML of the page
                'name': 'html',
                'type': 'string',
                'optional': True,
                'index': False
            },
            {
                # Generated by automated text summarization
                'name': 'summary',
                'type': 'string',
                'optional': True
            },
            {
                'name': 'top_image',
                'type': 'string',
                'optional': True,
            },
            {
                'name': 'technical',
                'type': 'bool',
                'optional': True
            }
        ],
        'default_sorting_field':
        'date'
    }
    client.collections.create(reliable_articles_schema)


if __name__ == "__main__":
    client = Client({
        'nodes': [{
            'host':
            'localhost',  # For Typesense Cloud use xxx.a1.typesense.net
            'port': '8108',  # For Typesense Cloud use 443
            'protocol': 'http'  # For Typesense Cloud use https
        }],
        'api_key':
        'xyz',
        'connection_timeout_seconds':
        2
    })
    create_schema(client)