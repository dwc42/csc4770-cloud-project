import React, { useEffect, useState } from "react";
export default function Matrix({ matrix }: { matrix: number[][]; }) {
	const [currentMatrix, setCurrentMatrix] = useState<number[][]>(matrix);
	const [nRowLength, setNRowLength] = useState<number>(matrix?.length ?? 0);;
	const [mColLength, setMColLength] = useState<number>(matrix[0]?.length ?? 0);;
	useEffect(() => {
		setCurrentMatrix(matrix);
		setNRowLength(matrix?.length ?? 0);
		setMColLength(matrix[0]?.length ?? 0);
	}, [matrix]);
	return (!nRowLength || !mColLength) ? <p>Invalid Matrix</p> : (
		<div style={{ padding: '20px' }}>

			{/* 2. The HTML Table Structure */}
			<table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #ddd' }}>
				<thead>
					<tr style={{ backgroundColor: '#f2f2f2', textAlign: 'left' }}>
						<th style={{ padding: '12px' }}></th>
						{
							Array.from({ length: mColLength }).map((_, i) => {
								return <th key={i} style={{ padding: '12px' }}>{i + 1}</th>;
							})
						}

					</tr>
				</thead>
				<tbody>
					{/* 3. Mapping over the data to create rows dynamically */}
					{Array.from({ length: nRowLength }).map((_, n) => {
						return <tr key={n} style={{ borderBottom: '1px solid #ddd' }}>
							<td style={{ padding: '12px', backgroundColor: '#f2f2f2', fontWeight: 'bold' }}>{n + 1}</td>
							{
								Array.from({ length: mColLength }).map((_, m) => {
									return <td key={m} style={{ padding: '12px' }}>{currentMatrix[n][m]}</td>;
								})
							}
						</tr>;
					}
					)}
				</tbody>
			</table>
		</div>
	);
} 