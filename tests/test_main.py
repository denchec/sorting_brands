import main as app


def test_average_rating_report_uses_tabulate(sample_rows, monkeypatch, capsys):
    captured = {}

    def fake_tabulate(data, headers, tablefmt, showindex):
        captured["data"] = data
        captured["headers"] = headers
        captured["tablefmt"] = tablefmt
        captured["showindex"] = showindex

        return "TABLE"

    monkeypatch.setattr(app.tabulate, "tabulate", fake_tabulate)

    app.average_rating_report(sample_rows)
    out = capsys.readouterr().out

    assert "TABLE" in out
    assert captured["headers"] == ["Brand", "Rating"]
    assert captured["tablefmt"] == "pipe"
    assert captured["showindex"] == "always"
    assert captured["data"] == [
        ["iphone 15 pro", "4.9"],
        ["galaxy s23 ultra", "4.8"],
        ["redmi note 12", "4.6"],
    ]


def test_main_unknown_report_prints_message(monkeypatch, capsys):
    monkeypatch.setattr(app, "read_csv", lambda files: [])
    app.main(["no-such"], ["products.csv"])
    out = capsys.readouterr().out

    assert "Report 'no-such' not found" in out


def test_main_happy_path(monkeypatch, sample_rows, capsys):
    monkeypatch.setattr(app, "read_csv", lambda files: sample_rows)
    monkeypatch.setattr(app.tabulate, "tabulate", lambda *a, **k: "OK")

    app.main(["average-rating"], ["products.csv"])
    out = capsys.readouterr().out

    assert "OK" in out
