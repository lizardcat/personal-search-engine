A simple personal search engine. This is a Python project for practicing iterating with increasing scope.

### Curent expansion path:

#### Level 1 — Core Indexing

- Input: set of local text files.
- Build: inverted index (word → list of file locations).
- Query: single keyword lookup.

#### Level 2 — Query Features

- Boolean operators (AND, OR, NOT).
- Phrase search (“exact string”).
- Case-insensitive and stopword removal.

#### Level 3 — Ranking & Scoring

- Word frequency counts.
- TF-IDF scoring.
- Sort results by relevance.

#### Level 4 — File Types & Sources

- Index PDFs, Word docs, Markdown, HTML.
- Configurable folder watcher for auto-indexing.

#### Level 5 — User Interface

- CLI tool with search prompt.
- Web UI with Flask: search bar + results list.

#### Level 6 — Advanced Retrieval

- Synonym expansion with WordNet.
- Fuzzy search (edit distance).
- Highlight matched terms in results.

#### Level 7 — Performance & Scale

- Incremental indexing.
- Compression for index storage.
- Multi-threaded crawling/indexing.

#### Level 8 — Semantic Layer

- Sentence embeddings for semantic search.
- Query expansion based on vector similarity.
- Hybrid search (keyword + semantic).

#### Level 9 — Personal Knowledge Base

- User annotations and tagging.
- Save queries as collections.
- Relevance feedback (user rates results → adjust ranking).

#### Level 10 — Full Personal Search Engine

- Web dashboard with filters, faceted search.
- API endpoint for programmatic queries.
- Cross-device sync of index and settings.
- Optionally distributed / peer-to-peer search across machines.

### Final structure (Maybe-ish)

```graphql
personal_search_engine/
│
├── search/                 # Core search logic
│   ├── __init__.py
│   ├── index.py            # Inverted index builder/updater
│   ├── query.py            # Query parsing & execution
│   ├── rank.py             # Ranking algorithms (TF-IDF, etc.)
│   └── semantic.py         # Embeddings / semantic search
│
├── crawler/                # File ingestion
│   ├── __init__.py
│   ├── filesystem.py       # Local file crawling
│   ├── parsers/            # File type parsers
│   │   ├── __init__.py
│   │   ├── text_parser.py
│   │   ├── pdf_parser.py
│   │   ├── docx_parser.py
│   │   └── html_parser.py
│   └── watcher.py          # Auto reindexing on file change
│
├── storage/                # Data persistence
│   ├── __init__.py
│   ├── db.py               # Index persistence (SQLite/JSON)
│   └── cache.py            # Optional: caching layer
│
├── interface/              # User-facing layers
│   ├── __init__.py
│   ├── cli.py              # Command-line interface
│   ├── web.py              # Flask/FastAPI web UI
│   └── api.py              # REST API for programmatic use
│
├── utils/                  # Shared utilities
│   ├── __init__.py
│   ├── config.py           # Config loader
│   └── text_processing.py  # Tokenization, stemming, stopwords
│
├── tests/                  # Unit and integration tests
│   ├── test_index.py
│   ├── test_query.py
│   └── test_crawler.py
│
├── scripts/                # Helper scripts for dev/admin
│   └── reindex_all.py
│
├── data/                   # Sample documents / test corpus
│
├── requirements.txt
├── pyproject.toml          # or setup.py for packaging
├── README.md
└── main.py                 # Entry point

```
