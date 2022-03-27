use pyo3::prelude::*;
use scraper::{Html, Selector};
use std::collections::HashMap;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(input: &str) -> PyResult<String> {
    Ok(filter(input))
}

/// A Python module implemented in Rust.
#[pymodule]
fn test_hoang(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}

fn filter(input: &str) -> String {
    let document = Html::parse_document(input);
    let selector = Selector::parse(
        r#"div[class="d-flex justify-content-between search-result-line py-3 px-3"] > div"#,
    )
    .unwrap();

    let mut bang_diem: HashMap<&str, &str> = HashMap::from([
        ("Toán", "-1"),
        ("Văn", "-1"),
        ("Lí", "-1"),
        ("Hóa", "-1"),
        ("Sinh", "-1"),
        ("Sử", "-1"),
        ("Địa", "-1"),
        ("GDCD", "-1"),
        ("Ngoại ngữ (<span>N1</span>)", "-1"),
        ("Ngoại ngữ (<span>N2</span>)", "-1"),
        ("Ngoại ngữ (<span>N3</span>)", "-1"),
        ("Ngoại ngữ (<span>N4</span>)", "-1"),
        ("Ngoại ngữ (<span>N5</span>)", "-1"),
        ("Ngoại ngữ (<span>N6</span>)", "-1"),
    ]);
    let temp = document.select(&selector);
    let mut vec = Vec::new();
    for element in temp {
        vec.push(element.inner_html());
    }

    for i in 0..vec.len() / 2 {
        bang_diem.insert(vec.get(i * 2).unwrap(), vec.get(i * 2 + 1).unwrap());
    }
    let mon = vec![
        "Toán",
        "Văn",
        "Lí",
        "Hóa",
        "Sinh",
        "Sử",
        "Địa",
        "GDCD",
        "Ngoại ngữ (<span>N1</span>)",
        "Ngoại ngữ (<span>N2</span>)",
        "Ngoại ngữ (<span>N3</span>)",
        "Ngoại ngữ (<span>N4</span>)",
        "Ngoại ngữ (<span>N5</span>)",
        "Ngoại ngữ (<span>N6</span>)",
    ];

    let mut result = String::new();
    for ele in mon {
        result.push_str(bang_diem[ele]);
        result.push(';');
    }
    result.push('\n');
    result
}
